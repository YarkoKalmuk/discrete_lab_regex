from __future__ import annotations
from abc import ABC, abstractmethod


class State(ABC):

    @abstractmethod
    def __init__(self) -> None:
        self.next_states: list[State] = []

    @abstractmethod
    def check_self(self, char: str) -> bool:
        """
        function checks whether occured character is handled by current ctate
        """
        pass

    def check_next(self, next_char: str) -> State | Exception:
        for state in self.next_states:
            if state.check_self(next_char):
                return state
        return False


class StartState(State):

    def __init__(self):
        super().__init__()

    def check_self(self, char):
        return super().check_self(char)


class TerminationState(State):

    def __init__(self):
        super().__init__()

    def check_self(self, char) -> bool:
        """
        function checks whether occured character is handled by current ctate
        """
        return False


class DotState(State):
    """
    state for . character (any character accepted)
    """
    def __init__(self):
        super().__init__()

    def check_self(self, char: str):
        # Implement
        return True


class AsciiState(State):
    """
    state for alphabet letters or numbers
    """

    def __init__(self, symbol: str) -> None:
        # Implement
        self.state_symbol = symbol
        super().__init__()

    def check_self(self, curr_char: str) -> State | Exception:
        return curr_char == self.state_symbol


class StarState(State):
    """
    state for * (one or more occurences)
    """

    def __init__(self, checking_state: State):
        # Implement
        self.checking_state = checking_state
        super().__init__()

    def check_self(self, char):
        for state in self.next_states:
            if state.check_self(char):
                return True

        return False


class PlusState(State):

    def __init__(self, checking_state: State):
        # Implement
        self.checking_state = checking_state
        super().__init__()

    def check_self(self, char):
        return self.checking_state.check_self(char)


class RegexFSM:
    curr_state: State = StartState()

    def __init__(self, regex_expr: str) -> None:

        prev_state = self.curr_state
        tmp_next_state = self.curr_state

        for char in regex_expr:
            tmp_next_state = self.__init_next_state(char, prev_state, tmp_next_state)
            prev_state.next_states.append(tmp_next_state)
            prev_state = tmp_next_state
        tmp_next_state.next_states.append(TerminationState())

    def __init_next_state(
        self, next_token: str, prev_state: State, tmp_next_state: State
    ) -> State:
        new_state = None

        match next_token:
            case next_token if next_token == ".":
                new_state = DotState()
            case next_token if next_token == "*":
                new_state = StarState(tmp_next_state)
                prev_state.next_states.append(new_state)

            case next_token if next_token == "+":
                # Implement
                new_state = PlusState(tmp_next_state)

            case next_token if next_token.isascii():
                new_state = AsciiState(next_token)

            case _:
                raise AttributeError("Character is not supported")

        return new_state

    def check_string(self, string: str) -> bool:
        curr_state = self.curr_state
        for char in string:
            new_state = curr_state.check_next(char)
            if new_state is False:
                return False
            curr_state = new_state

        for state in curr_state.next_states:
            if isinstance(state, TerminationState):
                return True
        return False



if __name__ == "__main__":
    # regex_pattern = "a*4.+hi"

    # regex_compiled = RegexFSM(regex_pattern)

    # print(regex_compiled.check_string("aaaaaa4uhi"))  # True
    # print(regex_compiled.check_string("4uhi"))  # True
    # print(regex_compiled.check_string("meow"))  # False
    regex_pattern = "br..kisyda.a"
    regex_compiled = RegexFSM(regex_pattern)

    print(regex_compiled.check_string("ababoy"))  # False
    print(regex_compiled.check_string("br=-kisydaaa"))  # True
    print(regex_compiled.check_string(""))  # False
