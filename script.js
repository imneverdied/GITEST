

$(document).ready(function () {
    $(Lpic).click(function () {
        let L = $(Lpic).attr("src");
        let R = $(Rpic).attr("src");
        $(Lpic).attr("src", pre(L));
        $(Rpic).attr("src", pre(R));

    });

    $(Rpic).click(function () {
        let L = $(Lpic).attr("src");
        let R = $(Rpic).attr("src");
        $(Lpic).attr("src", next(L));
        $(Rpic).attr("src", next(R));
    });

});

function next(input) {
    var PATH = input;
    var PIC = PATH.substring(PATH.lastIndexOf('/') + 1, PATH.length); //分割出圖片ID
    var PIC_NBR = PIC.substring(0, PIC.lastIndexOf('.'));
    parseInt(PIC_NBR);
    var returnNBR = parseInt(PIC_NBR) + 1;
    return '/src/航海王/' + padLeft(returnNBR, 3) + '.jpg';

}
function pre(input) {
    var PATH = input;
    var PIC = PATH.substring(PATH.lastIndexOf('/') + 1, PATH.length); //分割出圖片ID
    var PIC_NBR = PIC.substring(0, PIC.lastIndexOf('.'));
    parseInt(PIC_NBR);
    var returnNBR = parseInt(PIC_NBR) - 1;
    var rtnSTR = ''
    if (parseInt(returnNBR) == 0) {
        rtnSTR = input;
    }
    else {
        rtnSTR = '/src/航海王/' + padLeft(returnNBR, 3) + '.jpg';
    }

    return rtnSTR;

}

function padLeft(str, lenght) {
    if (str.length >= lenght)
        return str;
    else
        return padLeft("0" + str, lenght);
}