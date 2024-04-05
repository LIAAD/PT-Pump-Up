import pytest
from pt_pump_up.datasets.propbank_br import parser


def test_parser():
    dataset_dict = parser()

    assert dataset_dict['train'][0]['tokens'] == [
        'Brasília',
        'Pesquisa_Datafolha',
        'publicada',
        'hoje',
        'revela',
        'um',
        'dado',
        'supreendente',
        ':',
        'recusando',
        'uma',
        'postura',
        'radical',
        ',',
        'a',
        'esmagadora',
        'maioria',
        '(',
        '77',
        '%',
        ')',
        'de',
        'os',
        'eleitores',
        'quer',
        'o',
        'PT',
        'participando',
        'de',
        'o',
        'Governo',
        'Fernando_Henrique_Cardoso',
        '.',
    ]

    assert dataset_dict['train'][0]['srl_frames'] == [
        {
            'verb': 'revela',
            'frames': ['O', 'B-A0', 'I-A0', 'I-A0', 'B-V', 'B-A1', 'I-A1', 'I-A1', 'I-A1', 'I-A1', 'I-A1', 'I-A1', 'I-A1', 'I-A1', 'I-A1', 'I-A1', 'I-A1', 'I-A1', 'I-A1', 'I-A1', 'I-A1', 'I-A1', 'I-A1', 'I-A1', 'I-A1', 'I-A1', 'I-A1', 'I-A1', 'I-A1', 'I-A1', 'I-A1', 'I-A1', 'O']
        },
        {
            'verb': 'recusando',
            'frames': ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-V', 'B-A1', 'I-A1', 'I-A1', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
        },
        {
            'verb': 'quer',
            'frames': ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-AM-ADV', 'I-AM-ADV', 'I-AM-ADV', 'I-AM-ADV', 'O', 'B-A0', 'I-A0', 'I-A0', 'I-A0', 'I-A0', 'I-A0', 'I-A0', 'I-A0', 'I-A0', 'I-A0', 'B-V', 'B-A1', 'I-A1', 'B-AM-LOC', 'I-AM-LOC', 'I-AM-LOC', 'I-AM-LOC', 'I-AM-LOC', 'O']
        },
        {
            'verb': 'participando',
            'frames': ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-A0', 'I-A0', 'B-V', 'B-A1', 'I-A1', 'I-A1', 'I-A1', 'O']
        }
    ]
