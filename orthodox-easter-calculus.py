from Easterlib import EasterCalculus
from Easterlib import EasterRelated as erel

print("Default language is English press enter to continue\n За преминаване на Български въведете bg: ", end="")
lang = str(input()).lower()
select_year = "Select year to check for: "
if lang == "bg":
    select_year = "Изберете година за проверяване: "
print(select_year, end="")

year = int(input())
ec = EasterCalculus(year)
"""available options for EasterCalculus (ec):
1. ec.mode = applies to both calendar (Julian or Gregorian) and algorithm used for Easter's calculus.
available modes:
	"Julian" : Calculates Julian calendar's Easter according to the Meeus's algorithm
	"GaussJulian" : Calculates Julian calendar's Easter according to the Gauss' Julian Easter algorithm.
	"JulianInGregorian" : Calculates Julian Easter according Meeus' algorithm and aligns it to Gregorian Civil calendar (Suitable for Eastern Orthodox' Easter). Alignment for dates before Gregorian's calendar adoption is done according to adoption year and options set.
	"GaussJulianInGregorian" : Same as "JulianInGregorian", with Gauss' Julian algorithm used for calculation instead of Meeus'.
	"GaussGregorian" : Calculates Easter's day according to Gregorian calendar, using Gauss algorithm. Dates before Gregorian calendar's adoption are calculated according to the adoption year and options set.
	"AnonymousGregorian" : Same as "GaussGregorian", using Anonymous algorithm posted by New York Times correspondent instead.
	"AnonymousGregorianOptimized" : Same as "AnonymousGregorian", although New Scientist's optimization from 1961st are included in the algorithm.
	Note: all mode names are case insensitive.
	
2. ec.year = the year to check for
3. ec.adoptionYear = set the year since which Gregorian calendar is adopted defaults to 1582 (excluding)
4. ec.adoption = sets adoption mode, available options: "exclusive" : excludes the adoption year itself (default)
"inclusive" : includes the year of adoption
5. ec.gregPriorAdoptions : sets whether Gregorian dates should be calculated for years before adoption. (Defaults to False). If false, Julian Gauss dates are being return instead for any year before adoptions (applies to modes "JulianInGregorian","GaussJulianInGregorian", "GaussGregorian", "AnonymousGregorian", "AnonymousGregorianOptimized")

Result variables available:
	Note: all variables are being set on class initialization. If any option has been changed, ec.set() function must be called in order to update results.
	1. ec.date = [month, day]
	Returns Easter's day and month list according to provided configuration. 
	2. ec.day = int(day)
	Contains Easter's day in the month number.
	3. ec.month = int(month)
	Contains the Easter month's number.
	4. ec.leap = bool
	Contains information whether checked year is a leap year. True means leap, False not leap. The calculation is done according to calendar set (Julian or Gregorian).
	5. ec.year = int(year)
	The year processed.
	
Method functions available:
	1. ec.set(year = None, mode = None)
	If any change on configuration options is done, set()
function must be called to apply them on the result variables.
	2. ec.JulianCal(year)
	Returns Easter date's [month, day] list in Julian calendar, using Meeus' algorithm. Year option is required.
	3. ec.JulianInGregorian(month, day, year=None)
	Aligns Julian dates to Gregorian civil calendar. Dates before Gregorian calendar's adoption are calculated or not according to ec.gregPriorAdoption value. If year is None, the year from class variable ec.year is processed. [month, day] list is returned.
	4. ec.isLeap(year, mode = "Gregorian")
	Checks whether the year is leap. The mode options might be set to "Julian" or "Gregorian" in order to change leap year algorithm. Bool returned.
	5. ec.GaussAlgorithm(year, mode = "Julian")
	Processes given year according to Gauss algorithm. mode option with values "Julian" (default) and "Gregorian" to switch between calendars processed. [month, day] list is returned.
	6. ec.AnonymousGregorian(year, mode = "optimized")
	Processes given year according to the algorithm post in New York Times by a correspondent in 1876. mode option sets algorithm state to "optimized" (includes 1961 New Scientist's correction)(default) and the original 1867 version.The mode value is case sensitive. [month, day] list is returned.
	"""
ec.gregPriorAdoption = True
ec.set()
gjig = ec.GaussAlgorithm(year)
gjig = ec.JulianInGregorian(gjig[0], gjig[1], year)
jul = ec.JulianCal(year)
gjul = ec.GaussAlgorithm(year)
ggre = ec.GaussAlgorithm(year, "Gregorian")
agre = ec.AnonymousGregorian(year, "original")
agro = ec.AnonymousGregorian(year)
leapGreg = ec.leap
leapJul = ec.isLeap(year, "Julian")

if lang == "bg":
    out = "Православният Великден е на"
else:
    out = "The orthodox Easter is at"


def date_verbalize(dater, lang="en"):
    day = dater[1]
    month = dater[0]
    month_names = [None, "January", "February", "March", "April", "May", "June", "July", "August", "September",
                   "October", "November", "December"]

    ones_ending = ["th", "st", "nd", "rd", "th", "th", "th", "th", "th", "th"]
    day_ending = ones_ending[int(str(day)[-1])]
    if 9 < day < 20:
        day_ending = ones_ending[0]
    date = f"{month_names[month]}, {day}{day_ending}"

    if lang == "bg":
        month_names = [None, "Януари", "Февруари", "Март", "Април", "Май", "Юни", "Юли", "Август", "Септември",
                       "Октомври", "Ноември", "Декември"]

        ones_ending = ["-ти", "-ви", "-ри", "-ти", "-ти", "-ти", "-ти", "-ми", "-ми", "-ти"]
        if 9 < day < 20:
            day_ending = ones_ending[0]
        else:
            day_ending = ones_ending[int(str(day)[-1])]
        date = f"{str(day) + day_ending} {month_names[month]}"
    return date


def verbalize_true(boolean, lang="en"):
    if boolean:
        out = "is"
        if lang == "bg":
            out = "е"
    else:
        out = "is not"
        if lang == "bg":
            out = "не е"
    return out


gen = date_verbalize([ec.month, ec.day], lang)
gjig = date_verbalize(gjig, lang)
jul = date_verbalize(jul, lang)
gjul = date_verbalize(gjul, lang)
ggre = date_verbalize(ggre, lang)
agre = date_verbalize(agre, lang)
agro = date_verbalize(agro, lang)
print(("\n" + out + " " + gen + "\n").upper())
if lang == "bg":
    print(
        f"Юлиански в Грегориански: {gen}\nЮлиански Гаус в Грегориански: {gjig}\nЮлиански: {jul}\nЮлианску Гаус: {gjul}\nГрегориански Гаус: {ggre}\nАнонимен Грегориански: {agre}\nАнонимен Грегориански - подобрен: {agro}\nГрегорианската година {verbalize_true(leapGreg, lang)} високосна\nЮлианската година {verbalize_true(leapJul, lang)} високосна")
else:
    print(
        f"Julian in gregorian: {gen}\nGauss Julian in Gregorian: {gjig}\nJulian: {jul}\nJulian Gauss: {gjul}\nGregorian Gauss: {ggre}\nAnonymous Gregorian: {agre}\nAnonymous Gregorian optimized: {agro}\nThe Gregorian year {verbalize_true(leapGreg)} leap\nThe Julian year {verbalize_true(leapJul)} leap")
er = erel(year, ec.month, ec.day, "Gregorian")
