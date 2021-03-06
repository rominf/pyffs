from pyffs.core import State
from pyffs.automaton_generation import generate_universal_automaton


def test_generate_automaton_0():
    expected = [
        [State(-1, 0), State(-1, 0), State(0, 1)],
    ]

    automaton = generate_universal_automaton(0)

    assert automaton.matrix == expected
    assert automaton.bit_vectors == [(), (0,), (1,)]
    assert automaton.max_i_minus_e == [0]


def test_generate_automaton_1():
    expected = [
        [State(id=1, min_boundary=0),
         State(id=2, min_boundary=0),
         State(id=0, min_boundary=1),
         State(id=2, min_boundary=0),
         State(id=4, min_boundary=0),
         State(id=0, min_boundary=1),
         State(id=0, min_boundary=1),
         State(id=2, min_boundary=0),
         State(id=2, min_boundary=0),
         State(id=4, min_boundary=0),
         State(id=4, min_boundary=0),
         State(id=0, min_boundary=1),
         State(id=0, min_boundary=1),
         State(id=0, min_boundary=1),
         State(id=0, min_boundary=1)],
        [State(id=-1, min_boundary=0),
         State(id=-1, min_boundary=0),
         State(id=1, min_boundary=1),
         State(id=-1, min_boundary=0),
         State(id=-1, min_boundary=0),
         State(id=1, min_boundary=1),
         State(id=1, min_boundary=1),
         State(id=-1, min_boundary=0),
         State(id=-1, min_boundary=0),
         State(id=-1, min_boundary=0),
         State(id=-1, min_boundary=0),
         State(id=1, min_boundary=1),
         State(id=1, min_boundary=1),
         State(id=1, min_boundary=1),
         State(id=1, min_boundary=1)],
        [State(id=-1, min_boundary=0),
         State(id=-1, min_boundary=0),
         State(id=1, min_boundary=1),
         State(id=-1, min_boundary=0),
         State(id=1, min_boundary=2),
         State(id=1, min_boundary=1),
         State(id=2, min_boundary=1),
         State(id=-1, min_boundary=0),
         State(id=-1, min_boundary=0),
         State(id=1, min_boundary=2),
         State(id=1, min_boundary=2),
         State(id=1, min_boundary=1),
         State(id=1, min_boundary=1),
         State(id=2, min_boundary=1),
         State(id=2, min_boundary=1)],
        [State(id=-1, min_boundary=0),
         State(id=-1, min_boundary=0),
         State(id=1, min_boundary=1),
         State(id=-1, min_boundary=0),
         State(id=-1, min_boundary=0),
         State(id=1, min_boundary=1),
         State(id=1, min_boundary=1),
         State(id=-1, min_boundary=0),
         State(id=1, min_boundary=3),
         State(id=-1, min_boundary=0),
         State(id=1, min_boundary=3),
         State(id=1, min_boundary=1),
         State(id=3, min_boundary=1),
         State(id=1, min_boundary=1),
         State(id=3, min_boundary=1)],
        [State(id=-1, min_boundary=0),
         State(id=-1, min_boundary=0),
         State(id=1, min_boundary=1),
         State(id=-1, min_boundary=0),
         State(id=1, min_boundary=2),
         State(id=1, min_boundary=1),
         State(id=2, min_boundary=1),
         State(id=-1, min_boundary=0),
         State(id=1, min_boundary=3),
         State(id=1, min_boundary=2),
         State(id=2, min_boundary=2),
         State(id=1, min_boundary=1),
         State(id=3, min_boundary=1),
         State(id=2, min_boundary=1),
         State(id=4, min_boundary=1)]
    ]

    automaton = generate_universal_automaton(1)

    assert automaton.matrix == expected
    assert automaton.max_i_minus_e == [0, -1, 0, 1, 1]
