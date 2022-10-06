def convert_temp(unit_in, unit_out, temp):
    """Convert farenheit <-> celsius and return results.

    - unit_in: either "f" or "c" 
    - unit_out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)

    Return results of conversion, if any.

    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

    For example:

      convert_temp("c", "f", 0)  =>  32.0
      convert_temp("f", "c", 212) => 100.0
    """

    # YOUR CODE HERE
    faren = 'f'
    celcius = 'c'

    if unit_in != faren and unit_in != celcius:
      return f"Invalid unit {unit_in} should be 'f' or 'c'"

    if unit_out != faren and unit_out != celcius:
      return f"Invalid unit {unit_in} should be 'f' or 'c'"

    if unit_in == celcius and unit_out == faren:
      conversion = (temp * 1.8) + 32
      return int(conversion) , unit_out
    
    if unit_in == faren and unit_out == celcius:
      conversion = (temp - 32) * 0.556
      return int(conversion) , unit_out


print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")

