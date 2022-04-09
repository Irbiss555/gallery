let baseUrl = 'http://127.0.0.1:8000/'

$(document).ready(
    function () {
        $('#login-form').submit(
            function (e) {
                let inputs = $(this).serializeArray()
                let form = {}
                inputs.forEach(function (value) {
                    if (value['name'] === 'username') {
                        form.username = value['value']
                    } else if (value['name'] === 'password') {
                        form.password = value['value']
                    }
                })
                $.ajax(
                    {
                        method: 'POST',
                        url: `${baseUrl}api/login/`,
                        data: JSON.stringify({username: form.username, password: form.password}),
                        contentType: 'application/json',
                        success: function (response) {
                            localStorage.setItem('auth_token', response.token)
                        },
                        error: function (response) {
                            console.log(response)
                        }
                    }
                )
            })
        $('.btn-bookmark').click(
            function (e) {
                e.preventDefault()
                $.ajax({
                        method: 'POST',
                        url: baseUrl + `api/photo/${$(e.currentTarget).data('id')}/bookmark/`,
                        headers: {Authorization: 'Token ' + localStorage.getItem('auth_token')},
                        success: function (response) {
                            $(`#bookmark-txt-${$(e.currentTarget).data('id')}`).text(`${response.bookmarks_total} users bookmark photo`)
                            $(e.currentTarget).children('i').toggleClass('fa-solid fa-regular')
                        },
                        error: function (response) {
                            console.log(response)
                        }
                    }
                )
            }
        )
    }
)