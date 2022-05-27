# Easter Calendar
## _Dynamic Orthodox Church Calendar_
This repository aims to implement an Orthodox Church's Easter Calendar dynamically updating holidays during the year, according to the rules for their calculation.
This project is written in Python 3.

## Current files:

- Easterlib
- Orthodox Easter calculus

## Easterlib specifications:
##### _*Note: all these descriptions are presently contained in the exemplary orthodox_easter_calculus.py file._


* ### Options:
* __ec.mode__

	_Applies to both calendar (Julian or Gregorian) and algorithm used for Easter's calculus._
	##### _available modes:_
	- 1.	"Julian" : Calculates Julian calendar's Easter according to the Meeus's algorithm
	- 2.	"GaussJulian" : Calculates Julian calendar's Easter according to the Gauss' Julian Easter algorithm.
	- 3.	"JulianInGregorian" : Calculates Julian Easter according Meeus' algorithm and aligns it to Gregorian Civil calendar (Suitable for Eastern Orthodox' Easter). Alignment for dates before Gregorian's calendar adoption is done according to adoption year and options set.
	- 4.	"GaussJulianInGregorian" : Same as "JulianInGregorian", with Gauss' Julian algorithm used for calculation instead of Meeus'.
	- 5.	"GaussGregorian" : Calculates Easter's day according to Gregorian calendar, using Gauss algorithm. Dates before Gregorian calendar's adoption are calculated according to the adoption year and options set.
	- 6.	"AnonymousGregorian" : Same as "GaussGregorian", using Anonymous algorithm posted by New York Times correspondent instead.
	- 7.	"AnonymousGregorianOptimized" : Same as "AnonymousGregorian", although New Scientist's optimization from 1961st are included in the algorithm.
	- 8.	Note: all mode names are case insensitive.

* __ec.year__
    _the year to check for_
* __ec.adoptionYear__
    _Set the year since which Gregorian calendar is adopted defaults to 1582 (excluding)._
* __ec.adoption__
    _Sets adoption mode, available options:_
    - "exclusive" : excludes the adoption year itself (default)
    - "inclusive" : includes the year of adoption
* __ec.gregPriorAdoptions__
    _Sets whether Gregorian dates should be calculated for years before adoption. (Defaults to False)._
    - If false, Julian Gauss dates are being returned instead for any year before adoptions (applies to modes "JulianInGregorian","GaussJulianInGregorian", "GaussGregorian", "AnonymousGregorian", "AnonymousGregorianOptimized")

* ### Result variables available:
* ##### _Note: all variables are being set on class initialization. If any option has been changed, ec.set() function must be called in order to update results._

    1. **__ec.date = [month, day]__**
    _Returns Easter's day and month list according to provided configuration._
    2. **ec.day = int(day)**
    _Contains Easter's day in the month number._
    3. **ec.month = int(month)**
    _Contains the Easter month's number._
    4. **ec.leap = bool**
    _Contains information whether checked year is a leap year. True means leap, False not leap. The calculation is done according to calendar set (Julian or Gregorian)._
    5. **ec.year = int(year)**
    _The year processed._
    
* ### Method functions available:

	**1. ec.set(year = None, mode = None)**
		-  _If any change on configuration options is done, set() function must be called to apply them on the result variables._
    **2. ec.JulianCal(year)**
		-	_Returns Easter date's [month, day] list in Julian calendar, using Meeus' algorithm. Year option is required._
	**3. ec.JulianInGregorian(month, day, year=None)**
		-   _Aligns Julian dates to Gregorian civil calendar. Dates before Gregorian calendar's adoption are calculated or not according to ec.gregPriorAdoption value. If year is None, the year from class variable ec.year is processed. [month, day] list is returned._
	**4. ec.isLeap(year, mode = "Gregorian")**
		-   _Checks whether the year is leap. The mode options might be set to "Julian" or "Gregorian" in order to change leap year algorithm. Bool returned._
	**5. ec.GaussAlgorithm(year, mode = "Julian")**
		-   _Processes given year according to Gauss algorithm. mode option with values "Julian" (default) and "Gregorian" to switch between calendars processed. [month, day] list is returned._
	**6. ec.AnonymousGregorian(year, mode = "optimized")**
		-   _Processes given year according to the algorithm post in New York Times by a correspondent in 1876. mode option sets algorithm state to "optimized" (includes 1961 New Scientist's correction)(default) and the original 1867 version.The mode value is case sensitive. [month, day] list is returned._
