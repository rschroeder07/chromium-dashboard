from __future__ import division
from __future__ import print_function

# -*- coding: utf-8 -*-
# Copyright 2020 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import collections

import models


Process = collections.namedtuple(
    'Process',
    'name, description, applicability, stages')
# Note: A new feature always starts with intent_stage == INTENT_NONE
# regardless of process.  intent_stage is set to the first stage of
# a specific process when the user clicks a "Start" button and submits
# a form that sets intent_stage.


ProcessStage = collections.namedtuple(
    'ProcessStage',
    'name, description, progress_items, actions, '
    'incoming_stage, outgoing_stage')


def process_to_dict(process):
  """Return nested dicts for the nested namedtuples of a process."""
  process_dict = {
      'name': process.name,
      'description': process.description,
      'applicability': process.applicability,
      'stages': [stage._asdict() for stage in process.stages],
  }
  return process_dict


# This page generates a preview of an email that can be sent
# to a mailing list to announce an intent.
# The parameter "{feature_id}" is filled in by JS code.
INTENT_EMAIL_URL = '/admin/features/launch/{feature_id}?intent'


BLINK_PROCESS_STAGES = [
  ProcessStage(
      'Start incubation',
      'Create an initial WebStatus feature entry and kick off standards '
      'incubation (WICG) to share ideas.',
      ['Initial public proposal',
       'Motivation',
       'Spec repo',
      ],
      [],
      models.INTENT_NONE, models.INTENT_INCUBATE),

  ProcessStage(
      'Start prototyping',
      'Share an explainer doc and API. '
      'Start prototyping code in a public repo.',
      ['Explainer',
       'API design',
       'Code in repo',
       'Security review',
       'Privacy review',
       'Intent to Prototype email',
       'Spec reviewer',
      ],
      [('Draft Intent to Prototype email', INTENT_EMAIL_URL)],
      models.INTENT_INCUBATE, models.INTENT_IMPLEMENT),

  ProcessStage(
      'Dev trials and iterate on design',
      'Publicize availablity for developers to try. '
      'Provide sample code. '
      'Request feedback from browser vendors.',
      ['Samples',
       'Draft API overview',
       'Request signals',
       'External reviews',
       'Ready for Trial email',
      ],
      [('Draft Ready for Trial email', INTENT_EMAIL_URL)],
      models.INTENT_IMPLEMENT, models.INTENT_EXPERIMENT),

  ProcessStage(
      'Evaluate readiness to ship',
      'Work through a TAG review and gather vendor signals.',
      ['TAG review request',
       'Vendor signals',
       'Doc links',
       'Documentation signoff',
       'Estimated target milestone',
      ],
      [],
      models.INTENT_EXPERIMENT, models.INTENT_IMPLEMENT_SHIP),

  ProcessStage(
      'Origin Trial',
      '(Optional) Set up and run an origin trial. '
      'Act on feedback from partners and web developers.',
      ['OT request',
       'OT available',
       'OT results',
      ],
      [('Draft Intent to Experiment email', INTENT_EMAIL_URL)],
      models.INTENT_IMPLEMENT_SHIP, models.INTENT_EXTEND_TRIAL),

  ProcessStage(
      'Prepare to ship',
      'Lock in shipping milestone. Finalize docs and announcements. '
      'Further standardization.',
      ['Intent to Ship email',
       'Request to migrate incubation',
       'TAG issues addressed',
       'Three LGTMs',
       'Updated vendor signals',
       'Finalized target milestone',
      ],
      [('Draft Intent to Ship email', INTENT_EMAIL_URL)],
      models.INTENT_IMPLEMENT_SHIP, models.INTENT_SHIP),
  ]


BLINK_LAUNCH_PROCESS = Process(
    'New feature incubation',
    'Description of blink launch process',  # Not used yet.
    'When to use it',  # Not used yet.
    BLINK_PROCESS_STAGES)


BLINK_FAST_TRACK_STAGES = [
  ProcessStage(
      'Identify feature',
      'Create an initial WebStatus feature entry to implement part '
      'of an existing specification or combinaton of specifications.',
      ['Spec links',
      ],
      [],
      models.INTENT_NONE, models.INTENT_INCUBATE),

  ProcessStage(
      'Implement',
      'Check code into Chromium under a flag.',
      ['Code in Chromium',
      ],
      [],
      models.INTENT_INCUBATE, models.INTENT_IMPLEMENT),

  ProcessStage(
      'Dev trials and iterate on implementation',
      'Publicize availablity for developers to try. '
      'Provide sample code. '
      'Act on feedback from partners and web developers.',
      ['Samples',
       'Draft API overview (may be on MDN)',
       'Ready for Trial email',
       'Vendor signals',
       'Estimated target milestone',
      ],
      [('Draft Ready for Trial email', INTENT_EMAIL_URL)],
      models.INTENT_IMPLEMENT, models.INTENT_EXPERIMENT),

  ProcessStage(
      'Origin Trial',
      '(Optional) Set up and run an origin trial. '
      'Act on feedback from partners and web developers.',
      ['OT request',
       'OT available',
       'OT results',
      ],
      [('Draft Intent to Experiment email', INTENT_EMAIL_URL)],
      models.INTENT_EXPERIMENT, models.INTENT_EXTEND_TRIAL),

  ProcessStage(
      'Prepare to ship',
      'Lock in shipping milestone. Finalize docs and announcements. '
      'Further standardization.',
      ['Intent to Ship email',
       'Three LGTMs',
       'Documentation signoff',
       'Finalized target milestone',
      ],
      [('Draft Intent to Ship email', INTENT_EMAIL_URL)],
      models.INTENT_EXPERIMENT, models.INTENT_SHIP),
  ]


BLINK_FAST_TRACK_PROCESS = Process(
    'Existing feature implementation',
    'Description of blink fast track process',  # Not used yet.
    'When to use it',  # Not used yet.
    BLINK_FAST_TRACK_STAGES)


PSA_ONLY_STAGES = [
  ProcessStage(
      'Identify feature',
      'Create an initial WebStatus feature entry for a web developer '
      'facing change to existing code.',
      ['Spec links',
      ],
      [],
      models.INTENT_NONE, models.INTENT_INCUBATE),

  ProcessStage(
      'Implement',
      'Check code into Chromium under a flag.',
      ['Code in Chromium',
      ],
      [],
      models.INTENT_INCUBATE, models.INTENT_IMPLEMENT),

  ProcessStage(
      'Dev trials and iterate on implementation',
      'Publicize availablity for developers to try. '
      'Act on feedback from partners and web developers.',
      ['Ready for Trial email',
       'Vendor signals',
       'Estimated target milestone',
      ],
      [('Draft Ready for Trial email', INTENT_EMAIL_URL)],
      models.INTENT_IMPLEMENT, models.INTENT_EXPERIMENT),

  ProcessStage(
      'Prepare to ship',
      'Lock in shipping milestone.',
      ['Web facing PSA email',
       'One LGTM',
       'Finalize target milestone',
      ],
      [('Draft Intent to Ship email', INTENT_EMAIL_URL)],
      models.INTENT_EXPERIMENT, models.INTENT_SHIP),
  ]

PSA_ONLY_PROCESS = Process(
    'Web developer facing change to existing code',
    'Description of PSA process',   # Not used yet.
    'When to use it',  # Not used yet.
    PSA_ONLY_STAGES)


DEPRECATION_STAGES = [
  ProcessStage(
      'Write up motivation',
      'Create an initial WebStatus feature entry to deprecate '
      'an existing feature, including motivation and impact. '
      'Then, move existing Chromium code under a flag.',
      ['Link to existing feature',
       'Motivation',
       'Code in Chromium',
      ],
      [('Draft Intent to Deprecate and Remove email', INTENT_EMAIL_URL)],
      models.INTENT_NONE, models.INTENT_INCUBATE),

  # TODO(cwilso): Work out additional steps for flag defaulting to disabled.
  ProcessStage(
      'Dev trial',
      'Publicize deprecation and address risks. ',
      ['Ready for Trial email',
       'Vendor signals',
       'Estimated target milestone',
      ],
      [('Draft Ready for Trial email', INTENT_EMAIL_URL)],
      models.INTENT_INCUBATE, models.INTENT_EXPERIMENT),

  ProcessStage(
      'Prepare for Deprecation Trial',
      '(Optional) Set up and run a deprecation trial. ',
      ['DT request',
       'DT available',
       'Removal of DT',
      ],
      [('Draft Deprecation Trial email', INTENT_EMAIL_URL)],
      # TODO(jrobbins): Intent to extend deprecation.
      models.INTENT_EXPERIMENT, models.INTENT_EXTEND_TRIAL),

  ProcessStage(
      'Prepare to ship',
      'Lock in shipping milestone. '
      'Finalize docs and announcements before disabling feature by default.',
      ['Intent to Ship email',
       'Three LGTMs',
       'Finalized target milestone',
      ],
      [('Draft Intent to Ship email', INTENT_EMAIL_URL)],
      models.INTENT_EXPERIMENT, models.INTENT_SHIP),

  ProcessStage(
      'Remove code',
      'Once the feature is no longer available, remove the code.',
      ['Code removed',
      ],
      [],
      models.INTENT_SHIP, models.INTENT_REMOVED),
  ]


DEPRECATION_PROCESS = Process(
    'Feature deprecation',
    'Description of deprecation process',  # Not used yet.
    'When to use it',  # Not used yet.
    DEPRECATION_STAGES)


ALL_PROCESSES = {
    models.FEATURE_TYPE_INCUBATE_ID: BLINK_LAUNCH_PROCESS,
    models.FEATURE_TYPE_EXISTING_ID: BLINK_FAST_TRACK_PROCESS,
    models.FEATURE_TYPE_CODE_CHANGE_ID: PSA_ONLY_PROCESS,
    models.FEATURE_TYPE_DEPRECATION_ID: DEPRECATION_PROCESS,
    }


# These functions return a true value when the checkmark should be shown.
# If they return a string, and it starts with "http:" or "https:", it will
# be used as a link URL.
PROGRESS_DETECTORS = {
    'Initial public proposal':
    lambda f: f.initial_public_proposal_url,

    'Explainer':
    lambda f: f.explainer_links and f.explainer_links[0],

    'Samples':
    lambda f: f.sample_links and f.sample_links[0],

    'Doc links':
    lambda f: f.doc_links and f.doc_links[0],

    'TAG review request':
    lambda f: f.tag_review,

    'Vendor signals':
    lambda f: bool(
        f.ff_views != models.NO_PUBLIC_SIGNALS or
        f.safari_views != models.NO_PUBLIC_SIGNALS or
        f.ie_views != models.NO_PUBLIC_SIGNALS),

    'Estimated target milestone':
    lambda f: bool(f.shipped_milestone),

    'Code in Chromium':
    lambda f: f.impl_status_chrome in (
        models.IN_DEVELOPMENT, models.BEHIND_A_FLAG, models.ENABLED_BY_DEFAULT,
        models.ORIGIN_TRIAL, models.INTERVENTION),

    'Motivation':
    lambda f: bool(f.motivation),

    'Code removed':
    lambda f: f.impl_status_chrome == models.REMOVED,
}
