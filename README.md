# Easter Calendar
## _Dynamic Orthodox Church Calendar_
This repository aims to implement an Orthodox Church's Easter Calendar dynamically updating holidays during the year, according to the rules for their calculation.
This project is written in Python 3.

## Current files:

- Easterlib
- Orthodox Easter calculus

## Easterlib methods specifications
##### _*Note: all these descriptions are presently contained in the exemplary orthodox_easter_calculus.py file._

* ec.mode = applies to both calendar (Julian or Gregorian) and algorithm used for Easter's calculus.
available modes:
	- a.	"Julian" : Calculates Julian calendar's Easter according to the Meeus's algorithm
	- b.	"GaussJulian" : Calculates Julian calendar's Easter according to the Gauss' Julian Easter algorithm.
	c.	"JulianInGregorian" : Calculates Julian Easter according Meeus' algorithm and aligns it to Gregorian Civil calendar (Suitable for Eastern Orthodox' Easter). Alignment for dates before Gregorian's calendar adoption is done according to adoption year and options set.
	d.	"GaussJulianInGregorian" : Same as "JulianInGregorian", with Gauss' Julian algorithm used for calculation instead of Meeus'.
	e.	"GaussGregorian" : Calculates Easter's day according to Gregorian calendar, using Gauss algorithm. Dates before Gregorian calendar's adoption are calculated according to the adoption year and options set.
	f.	"AnonymousGregorian" : Same as "GaussGregorian", using Anonymous algorithm posted by New York Times correspondent instead.
	g.	"AnonymousGregorianOptimized" : Same as "AnonymousGregorian", although New Scientist's optimization from 1961st are included in the algorithm.
	h.	Note: all mode names are case insensitive.

* ec.year = the year to check for