
// Get search form and page links

let searchForm = document.getElementById('searchForm')
let pageLinks = document.getElementsByClassName('page-link')

//Check if search form exists 

if (searchForm) {
    for (let i = 0; i < pageLinks.length; i++) {

        pageLinks[i].addEventListener('click', function (e) {
            e.preventDefault();

            //Get data value 

            let page = this.dataset.page;
            searchForm.innerHTML += `<input type="hidden" name="page" value=${page} />`

            searchForm.submit();

        })
    }
}