"""
    test for homework 3
"""
import homework3
import pytest
import logging
import numpy
import statistics

LOGGER = logging.getLogger("__name__")


@pytest.fixture
def init_data() -> dict[dict]:
    """
        Giving data to test with
    :return: dict of dicts data
    """
    data = {
        "1": {"name": "tamar", "sex": "female", "age": 30},
        "2": {"name": "karen", "sex": "female", "age": 31},
        "3": {"name": "adham", "sex": "male", "age": 28},
        "4": {"name": "emad", "sex": "male", "age": 55},
        "5": {"name": "amal", "sex": "female", "age": 50}
    }
    print("connect to DB")  # simulation
    yield data
    print("\nDisconnect DB")  # simulation


@pytest.fixture
def get_all_ages_from_data(init_data) -> list[int]:
    """
    Init and return list of all ages
    :param init_data: the data
    :return: list of ages
    """
    l = [i['age'] for i in init_data.values()]
    return l


@pytest.fixture
def get_median_and_average(init_data) -> dict[str, float]:
    """
    Returning the median and average
    :param init_data: init data
    :return: dict of median and avg
    """
    return homework3.get_median_average(init_data)


@pytest.mark.smoke
@pytest.mark.parametrize("n", [20, 15, 26, None])
def test_print_values_above(init_data, get_all_ages_from_data, capfd, n):
    """
    Testing if its print the age above n
    :param init_data: init dict
    :param get_all_ages_from_data: list of ages from init dict
    :param capfd: buffer to console
    :param n: print ages above n
    :return:
    """
    LOGGER.info("Test if print_value_above prints correctly")
    homework3.print_values_above(init_data, n)
    out = capfd.readouterr().out
    if n is None:
        n = 0
    for age in get_all_ages_from_data:
        assert str(age) in out if age > n else str(age) not in out


@pytest.mark.smoke
def test_male_and_female_split_correct(init_data):
    """
    Testing if function split correct
    :param init_data: init data
    :return:
    """
    LOGGER.info("inside male\\female split test")
    male, female = homework3.split_male_female(init_data)
    for k, v in init_data.items():
        if v.get("sex") == 'male':
            assert k in male
        if v.get("sex") == 'female':
            assert k in female


@pytest.mark.smoke
def test_median_result(get_median_and_average, get_all_ages_from_data):
    """
    test if median result correct
    :param get_median_and_average: median result
    :param get_all_ages_from_data: list of ages
    :return:
    """
    LOGGER.info("Testing if median calculate correctly")
    assert get_median_and_average['median'] == statistics.median(get_all_ages_from_data)


@pytest.mark.smoke
def test_average_result(get_median_and_average, get_all_ages_from_data):
    """
     test if average result correct
    :param get_median_and_average: median result
    :param get_all_ages_from_data: list of ages
    :return:
    """
    LOGGER.info("Testing if average calculate correctly")
    assert get_median_and_average['average'] == numpy.average(get_all_ages_from_data)


if __name__ == '__main__':
    pass
