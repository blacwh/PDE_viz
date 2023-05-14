const isopic = document.getElementById('isopic');
const rangeV = document.getElementById('timestep');
const str_n = document.getElementById('nstr');


// let newSrc1 = '../static/jpg/iso_pic/iso_test/';
let newSrc1 = '';

str_n.addEventListener('change', () => {
    let options = $("#nstr option:selected");
    console.log(options.val());
    console.log(options.text());
    newSrc1 = '/static/jpg/iso_pic/pic_' + options.val() + '/';

})


rangeV.addEventListener('change', () => {
    let ts = Math.round(rangeV.value * 100);
    let newSrc2 = ts.toString() + '.png';
    if (ts < 10) {
        newSrc2 = '0' + newSrc2;
    }

    isopic.src = newSrc1 + newSrc2;

});




