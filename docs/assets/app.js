import EasterCalculus from "./easterLib.js"

function logics(){
    const tableBodyElement = document.querySelector("main table tbody")
    const yearHolder = document.getElementById("year-holder")
    const templateRow = tableBodyElement.querySelector("tr")
    const modes = ["JulianInGregorian","GaussJulianInGregorian","GaussGregorian","AnonymousGregorian","AnonymousGregorianOptimized","Julian","GaussJulian"]
    templateRow.remove()
    let lang = "bg"

    const translations = {
        bg:{
            year: "година",
            day: "ден",
            month:"месец",
            calendar:"календар",
            leap:"високосна",
            JulianInGregorian:"юлиански в грегориански",
            GaussJulianInGregorian:"юлиански в грегориански - гаус",
            GaussGregorian:" гргориански - гаус",
            AnonymousGregorian:"анонимен грегориански",
            AnonymousGregorianOptimized:" анонимен грегориански - оптимизиран",
            Julian:"юлиански",
            GaussJulian:"юлиански - гаус",
            months:[null,"януари","февруари","март","април","май","юни","юли","август","септември","октомври","ноември","декември"],
            bools:{true:"✔",false:"X"}

        }
    }

    function addRow(year,month,day,calendar,leap){
        const newRow = templateRow.cloneNode(true)
        const fields = newRow.querySelectorAll("td");
        [calendar,year,month,day,leap].forEach((el,idx)=>fields[idx].textContent = el)
        tableBodyElement.append(newRow)
    }

    function addData(year,mode){
        const {month,day,leap} = new EasterCalculus(year,mode)
        // addRow(year,month,day,mode.match(/[A-Z]?[a-z]*/gm).filter(el=>el).join(" "),leap)
        addRow(year,translations[lang].months[month],day,translations[lang][mode],translations[lang].bools[leap])
    }

    modes.forEach(mode=>addData(Number(yearHolder.textContent),mode))
}

logics()