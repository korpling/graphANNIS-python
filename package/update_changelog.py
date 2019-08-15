#!/usr/bin/env python3

import re
import os
import time

def replace_in_file(file, replacements):
  if len(replacements) == 0:
    return
  content = None
  with open(file, "r") as f_in:
    content = f_in.read()
  if content:
    for pattern, repl in replacements.items():
      content = re.sub(pattern, repl, content)
    with open(file, "w") as f_out:
      f_out.write(content)


if __name__ == "__main__":
    # get the version from the tag as provided by Travis
    if 'TRAVIS_TAG' in os.environ:
        release_tag = os.environ['TRAVIS_TAG']
        # remove "v" prefix
        if release_tag.startswith('v'):
            release_tag = release_tag[1:]
        
        version_header = '## [{}] - {} '.format(release_tag, time.strftime("%Y-%m-%d"))
        replace_in_file('CHANGELOG.md', {'## \[Unreleased\]' : '## [Unreleased]\n\n' + version_header })
    else:
        print("Not updating CHANGELOG.md since TRAVIS_TAG environment variable was not set")