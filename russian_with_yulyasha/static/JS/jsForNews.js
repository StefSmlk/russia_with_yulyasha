let img = document.getElementsByTagName('img');

img[1].setAttribute('width', '500');
img[2].classList.add('hidden-news');

for (let i = 3; i < img.length; i++) {
    if (i % 2 === 1) {
        img[i].setAttribute('width', '400');
    } else {
        img[i].classList.add('hidden-news');
    }
}



