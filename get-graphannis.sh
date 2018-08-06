#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"

if [ -z ${GRAPHANNIS_VERSION+x} ]; then
  # travis not set, but TRAVIS_TAG might be
  if [ -z ${TRAVIS_TAG+x} ]; then
    # also not set
    echo "Not a Travis deploy build"
  else
    # TRAVIS_TAG is set, set GRAPHANNIS_VERSION to its value
    GRAPHANNIS_VERSION=$TRAVIS_TAG
  fi
fi

if [ -z ${GRAPHANNIS_VERSION+x} ]; then
  # compile latest development
  mkdir ext/
  git clone https://github.com/corpus-tools/graphANNIS ext/graphANNIS
  cd ext/graphANNIS
  cargo build --release
  cd ../..
else
  # get released version
  echo "getting $GRAPHANNIS_VERSION"
  "$DIR"/package//download-release-binaries.sh "$GRAPHANNIS_VERSION"
fi