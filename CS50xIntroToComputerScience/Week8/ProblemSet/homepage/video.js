document.addEventListener('DOMContentLoaded', function() {
    let likeCount1 = 0;
    let dislikeCount1 = 0;
    let likeCount2 = 0;
    let dislikeCount2 = 0;

    document.querySelector('#likeButton1').addEventListener('click', function() {
        likeCount1 += 1;
        document.querySelector('#likeCount1').textContent = likeCount1;
    });

    document.querySelector('#dislikeButton1').addEventListener('click', function() {
        dislikeCount1 += 1;
        document.querySelector('#dislikeCount1').textContent = dislikeCount1;
    });

    document.querySelector('#likeButton2').addEventListener('click', function() {
        likeCount2 += 1;
        document.querySelector('#likeCount2').textContent = likeCount2;
    });

    document.querySelector('#dislikeButton2').addEventListener('click', function() {
        dislikeCount2 += 1;
        document.querySelector('#dislikeCount2').textContent = dislikeCount2;
    });


    let buttonHomepage = document.querySelector('#buttonHomepage');
    buttonHomepage.addEventListener('click', function() {
        window.location.href = 'index.html';
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
