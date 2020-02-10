from behave import *
from behave.runner import Context
from Pages.SearchPage import SearchPage
from Pages.DetailsPage import DetailsPage
from Pages.SummaryPage import SummaryPage
from Pages.ThankYouPage import ThankYouPage


@given('User go to the search page')
def step_impl(context: Context):
    SearchPage(context).go_to_page()


@given('User fill all mandatory fields')
def step_impl(context):
    SearchPage(context).fill_all_mandatory_fields()


@step('User click Search button')
def step_impl(context: Context):
    SearchPage(context).click_search_button()


@step('User check if form return proper results for our search setup')
def step_impl(context: Context):
    SearchPage(context).check_search_results()


@step('User chose one option from the list and click Rent')
def step_impl(context: Context):
    SearchPage(context).select_car_from_the_list()


@step('User check if the next page has proper value')
def step_impl(context: Context):
    DetailsPage(context).check_proper_values()


@step('User click button Rent1')
def step_impl(context):
    DetailsPage(context).click_search_button1()


@step('User check if all information on the Summary are proper')
def step_impl(context):
    SummaryPage(context).check_all_values()


@step('User fill all mandatory fields on Summary step')
def step_impl(context):
    SummaryPage(context).fill_all_fields()


@step('User click button Rent')
def step_impl(context):
    SummaryPage(context).click_search_button()


@step('User should receive confirmation regarding rent offer')
def step_impl(context):
    ThankYouPage(context).check_confirmation()
