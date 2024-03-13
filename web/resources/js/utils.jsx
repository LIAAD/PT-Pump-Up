

export const ToProperCase = (str) => {
    return str.replace(
        /\w\S*/g,
        function (txt) {
            return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
        }
    );
}
//There is 4 digits in the string provided by the bibtex
export const ExtractYearFromBibtex = (bibtex) => {
    const regex = /(\d{4})/g;
    const year = bibtex.match(regex);
    return year[0];
}