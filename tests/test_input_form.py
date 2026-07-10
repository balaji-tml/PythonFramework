from pages.home_page import HomePage
from pages.input_form_page import InputFormPage

def test_submit_form(driver):

    home = HomePage(driver)
    home.open_input_form()

    form = InputFormPage(driver)

    form.fill_form(
        "John",
        "john@test.com",
        "Password123",
        "ABC Ltd",
        "abc.com",
        "IN",
        "Bangalore",
        "123,BTM Layout,",
        "Near Indian Petrol Outlet",
        "Karnataka",
        "560089"
    )

    form.submit()

    assert "Thanks" in form.success_message()


