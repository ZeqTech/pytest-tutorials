import pytest
import random


@pytest.fixture(scope="session")
def session_fixture() -> int:
    print("\nSetup: session fixture")
    return random.randint(21, 30)


@pytest.fixture(scope="package")
def package_fixture() -> int:
    print("\nSetup: package fixture")
    return random.randint(21, 30)


@pytest.fixture(scope="module")
def module_fixture() -> int:
    print("\nSetup: module fixture")
    return random.randint(11, 20)


@pytest.fixture(scope="class")
def class_fixture() -> int:
    print("\nSetup: class fixture")
    return random.randint(21, 30)


@pytest.fixture(scope="function")
def function_fixture() -> int:
    print("\nSetup: function fixture")
    return random.randint(1, 10)
