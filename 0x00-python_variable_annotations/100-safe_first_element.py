from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if len(lst) > 0:
        return lst[0]
    else:
        return None
