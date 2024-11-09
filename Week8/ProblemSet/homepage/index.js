document.addEventListener('DOMContentLoaded', function() {
    let input = document.querySelector('#nameInput');
    let nameParagraph = document.querySelector('#greeting');
    nameParagraph.innerHTML = 'Hello, David?';

    input.addEventListener('keyup', function(event) {
        if (input.value) {
            nameParagraph.innerHTML = `Hello, ${input.value}`;
        } else {
            nameParagraph.innerHTML = 'Hello, David?';
        }
    });

    let buttonDontPress = document.querySelector('#buttonDontPress');
    let duckImage = document.querySelector('#duckImage');
    let scaryAudio = document.querySelector('#scaryAudio');

    buttonDontPress.addEventListener('click', function() {
        duckImage.style.display = 'block';
        scaryAudio.play();

        setTimeout(function() {
            window.location.href = 'index.html';
        }, 4000);
    });

    let buttonVideo = document.querySelector('#buttonVideo');
    buttonVideo.addEventListener('click', function() {
        window.location.href = 'video.html';
    });
    let buttonList = document.querySelector('#buttonList');
    buttonList.addEventListener('click', function() {
        window.location.href = 'list.html';
    });
    let buttonCallender = document.querySelector('#buttonCallender');
    buttonCallender.addEventListener('click', function() {
        window.location.href = 'callender.html';
    });

});
