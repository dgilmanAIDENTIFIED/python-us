def pytest_addoption(parser):
    parser.addoption(
        "--timezone",
        action="store_true",
        dest="timezone",
        default=False,
        help="enable checking timezone data against IANA database",
    )
    parser.addoption(
        "--dc-statehood",
        action="store_true",
        dest="dc_statehood",
        default=False,
        help="enable DC statehood tests (you must export DC_STATEHOOD envvar)",
    )
    parser.addoption(
        "--shapefile-urls",
        action="store_true",
        dest="shapefile_urls",
        default=False,
        help="test for existence of shapefile URLs on census server",
    )
