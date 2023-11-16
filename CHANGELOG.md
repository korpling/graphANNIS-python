The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- Update to graphANNIS 2.4.8.
- Changed minimal Python version to 3.8

## [2.1.0] - 2022-06-01 

### Changed

- Update to graphANNIS 2.1.0 This does change the graphANNIS C-API (see
  <https://github.com/korpling/graphANNIS/blob/main/CHANGELOG.md#200---2022-03-29>)
  but does not actually the exported functions of the Python API.

## [1.4.1] - 2021-12-09 

### Changed

- Update to graphANNIS 1.4.1

## [0.32.0] - 2021-08-09 

### Added

- Add export API

## [0.30.0] - 2020-11-06 

### Changed

- Updated graphANNIS version to 0.30.0

## [0.27.0] - 2020-03-06 

### Changed

- Updated graphANNIS version to 0.26.0

## [0.26.0] - 2019-11-25 

- Support multiple corpora in find, count, count\_extra and frequency

## [0.25.0] - 2019-11-15 

### Changed

- Updated graphANNIS version to 0.24.0

## [0.24.0] - 2019-10-18 

### Added

- Subgraph now accepts a segmentation name as context parameter.

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
