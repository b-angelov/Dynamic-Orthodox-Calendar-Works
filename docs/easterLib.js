class EasterCalculus {
    constructor(year = 2022, mode = "JulianInGregorian",
                adoption = {"adoptionYear": 1582, "adoption": "exclusive", "gregPriorAdoption": false}) {
        this.year = year
        this.leap = this.isLeap(year, mode)
        this.adoptionYear = adoption["adoptionYear"]
        this.adoption = adoption["adoption"]
        this.gregPriorAdoption = adoption["gregPriorAdoption"]
        this.mode = mode.toLowerCase()
        this.month = null
        this.day = null
        this.date = null
        this.sets(year)
    }

    sets(year = null, mode = null) {
        let date = []
        year = year ? year : this.year
        mode = mode ? mode : this.mode
        mode = mode.toLowerCase()
        if (mode === "Julian".toLowerCase()) {
            this.date = this.JulianCal(year)
            this.leap = this.isLeap(year, "Julian")
        } else if (mode === "JulianInGregorian".toLowerCase()) {
            date = this.JulianCal(year)
            this.date = this.JulianInGregorian(date[0], date[1], year)
        } else if (mode === "GaussGregorian".toLowerCase()) {
            this.date = this.GaussAlgorithm(year, "Gregorian")
        } else if (mode === "GaussJulian".toLowerCase() || !this.gregPriorAdoption) {
            this.date = this.GaussAlgorithm(year)
            this.leap = this.isLeap(year, "Julian")
        } else if (mode === "GaussJulianInGregorian".toLowerCase()) {
            date = this.GaussAlgorithm(year)
            this.date = this.JulianInGregorian(date[0], date[1], year)
        } else if (mode === "AnonymousGregorian".toLowerCase()) {
            this.date = this.AnonymousGregorian(year, "original")
        } else if (mode === "AnonymousGregorianOptimized".toLowerCase()) {
            this.date = this.AnonymousGregorian(year)
        }

        this.month = this.date[0]
        this.day = this.date[1]
        this.year = year
        return date
    }

    JulianCal(year) {
        const a = year % 4
        const b = year % 7
        const c = year % 19
        const d = (19 * c + 15) % 30
        const e = (2 * a + 4 * b - d + 34) % 7
        const month = Math.trunc((d + e + 114) / 31)
        const day = ((d + e + 114) % 31) + 1
        return [month, day]
    }

    JulianInGregorian(month, day, year = null) {
        if (!year) {
            year = this.year
        }
        let increase = 0
        const adoptionYear = this.__adoption_year()

        if (year > adoptionYear || this.gregPriorAdoption) {
            increase = Math.trunc(year / 100) - Math.trunc(year / 400) - 2
        }
        day += increase
        const month_length = this.__month_length(month, year)
        if (day > month_length) {
            day = day % month_length
            if (month + 1 <= 12) {
                month += 1
            } else {
                month = 1
                year += 1
            }
        }
        return [month, day, year]
    }

    __adoption_year() {
        let adoptionYear = this.adoptionYear
        if (this.adoption !== "exclusive") {
            adoptionYear -= 1
        }
        return adoptionYear
    }

    __month_length(month, year = None, calendar = "Gregorian") {
        const month_length = [null, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (year && this.isLeap(year, calendar)) {
            month_length[2] = 29
        }
        return month_length[month]
    }

    isLeap(year, mode = "Gregorian") {
        mode = mode.toLowerCase()
        if ((year % 4 === 0 && (mode === "Julian".toLowerCase() || mode === "JulianGauss".toLowerCase())) || (year % 4 === 0 && year % 100 !== 0)
            || (year % 400 === 0)) {
            return true
        }

        return false
    }

    GaussAlgorithm(year, mode = "Julian") {
        if (this.gregPriorAdoption === false && this.__adoption_year() >= year) {
            mode = "Julian"
        }
        mode = mode.lower()
        let a = year % 19
        let b = year % 4
        let c = year % 7
        let M = 15
        let N = 6
        if (mode === "Gregorian".toLowerCase()) {
            let k = Math.trunc(year / 100)
            let p = Math.trunc((13 + 8 * k) / 25)
            let q = Math.trunc(k / 4)
            M = (15 - p + k - q) % 30
            N = (4 + k - q) % 30
        }
        let d = (19 * a + M) % 30
        let e = (2 * b + 4 * c + 6 * d + N) % 7
        if (22 + d + e <= 31) {
            let month = 3
            let day = 22 + d + e
        } else {
            let month = 4
            let day = d + e - 9
        }

        if (d === 28 && e === 6 && (11 * M - 11) % 30 < 19 && day === 25) {
            let day = 18
        } else if (d === 29 && e === 6 && day === 26) {
            let day = 19
        }
        return [month, day]
    }

    AnonymousGregorian(year, mode = "optimized") {
        if (this.gregPriorAdoption === false && this.__adoption_year() >= year) {
            return this.GaussAlgorithm(year)
        }
        mode = mode.lower()
        let a = year % 19
        let b = Math.trunc(year / 100)
        let c = year % 100
        let d = Math.trunc(b / 4)
        let e = b % 4
        if (mode === "optimized") {
            let g = Math.trunc((8 * b + 13) / 25)
        } else {
            let f = Math.trunc((b + 8) / 25)
            let g = Math.trunc((b - f + 1) / 3)
        }
        let h = (19 * a + b - d - g + 15) % 30
        let i = Math.trunc(c / 4)
        let k = c % 4
        let l = (32 + 2 * e + 2 * i - h - k) % 7
        if (mode === "optimized") {
            let m = Math.trunc((a + 11 * h + 19 * l) / 433)
            let n = Math.trunc((h + l - 7 * m + 90) / 25)
            let p = (h + l - 7 * m + 33 * n + 19) % 32
        } else {
            let m = Math.trunc((a + 11 * h + 22 * l) / 451)
            let n = Math.trunc((h + l - 7 * m + 114) / 31)
            let o = (h + l - 7 * m + 114) % 31
            let p = o + 1
        }
        let month = n
        let day = p
        return [month, day]
    }
}

console.log(new EasterCalculus(2023))