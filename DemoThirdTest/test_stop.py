import pytest

class TestMath:
    def test_divide_number(self):
        pytest.xfail(reason="Need to investigate")
        num = 10
        result = 10 +10
        assert result == num/num

    # @pytest.mark.xfail(reason="You are using wrong calculation")
    def test_square_numbers(self):
        num = 10
        result = num + num
        assert  result == num ** 2

    # @pytest.mark.xfail(run=False)
    def test_run_false(self):
        num = 10
        result = num + num
        assert  result == num ** 2

    # @pytest.mark.xfail(run=True)
    def test_run_true(self):
        num = 10
        result = num * num
        assert result == num ** 2