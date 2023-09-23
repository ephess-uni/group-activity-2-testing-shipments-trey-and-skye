# Create your pytest cases here

from src.shipment_pairs import remove_intra, collect_pairs
import pytest

# Write tests for remove_intra

__input = [
            ['AB', 'BA', 9],
            ['AB', 'BA', 3],
            ['BA', 'AB', 6],
            ['AB', 'AB', 5]
        ]

__expected = [
                ['AB', 'BA', 9],
                ['AB', 'BA', 3],
                ['BA', 'AB', 6]
        ]
@pytest.mark.parametrize(
    'test_input, expected',
    [
        (__input, __expected)
    ]
)
def test_remove_intra(test_input, expected):
    assert remove_intra(test_input) == expected






# Write tests for collect_pairs