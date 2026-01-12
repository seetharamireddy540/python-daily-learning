"""
Python Classes Tutorial: Regular, Data, and Immutable Classes
"""
from dataclasses import dataclass, field
from typing import List, Optional


# 1. REGULAR CLASS
class Person:
    """Traditional class with manual __init__ and methods"""
    
    def __init__(self, name: str, age: int, email: Optional[str] = None):
        self.name = name
        self.age = age
        self.email = email
        self._id = id(self)  # Private attribute
    
    def __str__(self) -> str:
        return f"Person(name='{self.name}', age={self.age})"
    
    def __repr__(self) -> str:
        return f"Person('{self.name}', {self.age}, '{self.email}')"
    
    def greet(self) -> str:
        return f"Hello, I'm {self.name}"
    
    def have_birthday(self) -> None:
        """Mutable method - changes state"""
        self.age += 1


# 2. DATA CLASS (Python 3.7+)
@dataclass
class Student:
    """Data class - automatically generates __init__, __repr__, __eq__"""
    name: str
    age: int
    grades: List[float] = field(default_factory=list)
    email: Optional[str] = None
    
    def __post_init__(self):
        """Called after __init__ for additional setup"""
        if self.age < 0:
            raise ValueError("Age cannot be negative")
    
    def add_grade(self, grade: float) -> None:
        self.grades.append(grade)
    
    def average_grade(self) -> float:
        return sum(self.grades) / len(self.grades) if self.grades else 0.0


# 3. IMMUTABLE DATA CLASS
@dataclass(frozen=True)
class Point:
    """Immutable data class - cannot modify after creation"""
    x: float
    y: float
    
    def distance_from_origin(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def move(self, dx: float, dy: float) -> 'Point':
        """Returns new Point instead of modifying current one"""
        return Point(self.x + dx, self.y + dy)


# 4. IMMUTABLE CLASS WITH SLOTS
class ImmutableUser:
    """Memory-efficient immutable class using __slots__"""
    __slots__ = ('_name', '_email', '_created_at')
    
    def __init__(self, name: str, email: str, created_at: str):
        object.__setattr__(self, '_name', name)
        object.__setattr__(self, '_email', email)
        object.__setattr__(self, '_created_at', created_at)
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def email(self) -> str:
        return self._email
    
    @property
    def created_at(self) -> str:
        return self._created_at
    
    def __setattr__(self, name, value):
        raise AttributeError("Cannot modify immutable object")
    
    def __repr__(self) -> str:
        return f"ImmutableUser('{self.name}', '{self.email}', '{self.created_at}')"


# 5. CLASS WITH PROPERTIES AND VALIDATION
class BankAccount:
    """Class demonstrating properties and validation"""
    
    def __init__(self, account_number: str, initial_balance: float = 0.0):
        self.account_number = account_number
        self._balance = initial_balance
    
    @property
    def balance(self) -> float:
        """Getter for balance"""
        return self._balance
    
    @balance.setter
    def balance(self, amount: float) -> None:
        """Setter with validation"""
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = amount
    
    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
    
    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            return False
        self._balance -= amount
        return True


if __name__ == "__main__":
    print("=== REGULAR CLASS ===")
    person = Person("Alice", 30, "alice@email.com")
    print(person)
    print(person.greet())
    person.have_birthday()
    print(f"After birthday: {person}")
    
    print("\n=== DATA CLASS ===")
    student = Student("Bob", 20)
    student.add_grade(85.5)
    student.add_grade(92.0)
    print(student)
    print(f"Average grade: {student.average_grade()}")
    
    print("\n=== IMMUTABLE DATA CLASS ===")
    point1 = Point(3.0, 4.0)
    print(f"Point: {point1}")
    print(f"Distance from origin: {point1.distance_from_origin()}")
    
    # This creates a new point, doesn't modify the original
    point2 = point1.move(1.0, 1.0)
    print(f"Original point: {point1}")
    print(f"Moved point: {point2}")
    
    # Trying to modify will raise an error
    try:
        point1.x = 5.0  # This will fail
    except AttributeError as e:
        print(f"Cannot modify immutable object: {e}")
    
    print("\n=== IMMUTABLE CLASS WITH SLOTS ===")
    user = ImmutableUser("Charlie", "charlie@email.com", "2024-01-01")
    print(user)
    print(f"User name: {user.name}")
    
    try:
        user.name = "David"  # This will fail
    except AttributeError as e:
        print(f"Cannot modify: {e}")
    
    print("\n=== CLASS WITH PROPERTIES ===")
    account = BankAccount("12345", 1000.0)
    print(f"Initial balance: ${account.balance}")
    
    account.deposit(500.0)
    print(f"After deposit: ${account.balance}")
    
    success = account.withdraw(200.0)
    print(f"Withdrawal successful: {success}, Balance: ${account.balance}")
    
    try:
        account.balance = -100  # This will fail validation
    except ValueError as e:
        print(f"Validation error: {e}")