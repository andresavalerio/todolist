from src.inmemoryuserrepository import InMemoryUserRepository
from src.signup import SignUp

def test_signup_with_valid_data():
    user_repo = InMemoryUserRepository()
    user_name = 'Joe Doe'
    user_email = 'joe@doe.com'
    user_password = '1234'
    usecase = SignUp(user_repo)
    usecase.perform(user_name, user_email, user_password)
    assert user_repo.find_by_email(user_email).name == user_name