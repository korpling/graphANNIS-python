The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.23.1] - 2019-09-02 

### Fixed

-  `frequency(...)` did not return all rows, but used the number of columns internally

## [0.23.0] - 2019-08-16 

### Changed

-  From this version on, graphANNIS-python follows its own versioning scheme independent of the graphANNIS core library.
-  API now only accepts a single corpus name in `find` and `count` instead of a list of corpus names

### Added

- `frequency(...)` function in the corpus storage manager
- `count_extra(...)` function in the corpus storage manager