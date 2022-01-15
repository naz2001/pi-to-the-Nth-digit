# pi to the Nth digit

Write a script to find pi to the Nth digit. This was one of the daily challenges of Day 6 MLH Local Hack Day January 2022.



## How does it work?

User must enter the number of the decimals to which the value of pi should be calculated.

The math.acos() method returns the arc cosine value of a number. The value of Π is calculated using acos() function which returns a numeric value between [-Π, Π].Since using acos(0.0) will return the value for 2*Π. Therefore to get the value of Π:
                                  <div align="center"> pi = round(2*acos(0.0));</div>

The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.

## Example

<p align="center">
  <img src="https://user-images.githubusercontent.com/57052959/149608739-a7d5b79a-31d1-4a4f-b87e-302f5691265e.JPG" alt="output">
</p>
