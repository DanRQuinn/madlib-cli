def parse_template(template):
  """
  Parses a template string and returns a Template object.

  Args:
    template: The template string to parse.

  Returns:
    A Template object.
  """

  # Import the Template class from the string module.
  from string import Template

  # Create a Template object using the template string as an argument.
  template_object = Template(template)

  # Return the Template object.
  return template_object

