document.addEventListener('DOMContentLoaded', function() {
    let addItemButton = document.querySelector('#addItem');
    let newItemInput = document.querySelector('#newItem');

    function addItem() {
        let newItemText = newItemInput.value;
        if (newItemText.trim() !== '') {
            let listItem = document.createElement('li');
            listItem.textContent = newItemText;

            let deleteButton = document.createElement('button');
            deleteButton.textContent = 'X';
            deleteButton.onclick = function() {
                listItem.remove();
            };

            listItem.appendChild(deleteButton);
            document.querySelector('#itemList').appendChild(listItem);
            newItemInput.value = '';
        }
    }

    addItemButton.addEventListener('click', addItem);

    newItemInput.addEventListener('keypress', function(event) {
        if (event.keyCode === 13) {
            addItem();
        }
    });

    let buttonHomepage = document.querySelector('#buttonHomepage');
    buttonHomepage.addEventListener('click', function() {
        window.location.href = 'index.html';
    });

    let buttonVideo = document.querySelector('#buttonVideo');
    buttonVideo.addEventListener('click', function() {
        window.location.href = 'video.html';
    });

    let buttonCallender = document.querySelector('#buttonCallender');
    buttonCallender.addEventListener('click', function() {
        window.location.href = 'callender.html';
    });
});
