#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C0330,C0103
"""UKMDB Worker.

Usage: ukm_worker [--help] [--debug ...]

Options:
  -d --debug               Show debug information (maybe multiple).

  ukm_worker (-h | --help)
  ukm_worker --version

"""

from __future__ import absolute_import
import logging
from pprint import pformat
from celery import Celery
from docopt import docopt
from ukmdb_settings import settings
from ukmdb_worker import __version__
from ukmdb_worker import queues
from ukmdb_worker.base import set_debug_level


ukmdb_log = logging.getLogger("ukmdb")


def get_mod_version():
    return __version__


app = Celery('worker',
             broker=settings.AMQP_BROKER_URL,
             )

queues.setup(app)


@app.task(serializer='json',
          ignore_result=True,
          queue='ukmdb_all_errors',
          routing_key='*.info'
          #          exchange='ukmdb_error_in',
          #          routing_key='#'
          )
def ukmdb_info(msg):
    print("ukmdb_info: '%s'" % str(msg))


@app.task(serializer='json',
          ignore_result=True,
          queue='ukmdb_all_errors',
          #   exchange='ukmdb_error_in',
          routing_key='*.error'
          )
def ukmdb_error(msg):
    print("ukmdb_error: '%s'" % str(msg))


@app.task(serializer='json',
          name='ukmdb.add_object',
          queue='ukmdb_monitoring01',
          exchange='ukmdb_all_in',
          routing_key='#',
          bind=True
          )
def add_object(self, msg):
    ukmdb_log.info("-------> self.request: '%s'", pformat(self.request))
    ukmdb_log.info("worker # add_object: '%s'", str(msg))


@app.task(serializer='json',
          name='ukmdb.edit_object',
          queue='ukmdb_monitoring01',
          exchange='ukmdb_all_in',
          routing_key='#',
          bind=True
          )
def edit_object(self, msg):
    ukmdb_log.info("-------> self.request: '%s'", pformat(self.request))
    ukmdb_log.info("worker # edit_object: '%s'", str(msg))


@app.task(serializer='json',
          name='ukmdb.del_object',
          queue='ukmdb_monitoring01',
          exchange='ukmdb_all_in',
          routing_key='#',
          bind=True
          )
def del_object(self, msg):
    ukmdb_log.info("-------> self.request: '%s'", pformat(self.request))
    ukmdb_log.info("worker # worker:::del_object: '%s'", str(msg))


def main():
    arguments = docopt(__doc__, options_first=True, version=__version__)
    set_debug_level(ukmdb_log, arguments)

    ukmdb_log.debug(u'program start')
    app.start()

    exit("See 'ukm_worker --help'.")
