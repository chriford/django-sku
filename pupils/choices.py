from enum import Enum

class StatusChoices(Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    REJECTED = "REJECTED"
    
    @classmethod
    def choices(cls):
        choice_tuple = (tuple(cls.COMPLETED, choice.value) for choice in cls)
        return choice_tuple

