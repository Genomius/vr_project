jQuery(document).ready(function() {
    var max_price_input = $('input#catalog-price-max'),
    min_price_input = $('input#catalog-price-min');

    var connectSlider = document.getElementById('price-slider');
    noUiSlider.create(connectSlider, {
        start: [parseInt(min_price_input.attr('placeholder')), parseInt(max_price_input.attr('placeholder'))],
        connect: false,
        range: {
            'min': parseInt(min_price_input.attr('placeholder')),
            'max': parseInt(max_price_input.attr('placeholder'))
        }
    });

    var connectBar = document.createElement('div'),
    connectBase = connectSlider.querySelector('.noUi-base');

    // Give the bar a class for styling and add it to the slider.
    connectBar.className += 'price-slider';
    connectBase.appendChild(connectBar);

    connectSlider.noUiSlider.on('update', function( values, handle, a, b, handlePositions ) {
        var offset = handlePositions[handle];

        // Right offset is 100% - left offset
        if ( handle === 1 ) {
            offset = 100 - offset;
        }

        // Pick left for the first handle, right for the second.
        connectBar.style[handle ? 'right' : 'left'] = offset + '%';

        var value = values[handle];

        if ( handle ) {
            $(max_price_input).val(Math.round(value));
        } else {
            $(min_price_input).val(Math.round(value));
        }

        $.ajax({
            type: "POST",
            url: '/catalog/ajax/',
            dataType: 'json',
            data: {
                'max_price': $(max_price_input).val(),
                'min_price': $(min_price_input).val()
            },
            success: function(data) {
                $('.content').html(data);
            },
            error: function(err){
                console.error(err);
            }
        });
    });

    $(max_price_input).on('change', function(){
        connectSlider.noUiSlider.set([null, this.value]);
    });

    $(min_price_input).on('change', function(){
        connectSlider.noUiSlider.set([this.value, null]);
    });



        $('body').on('click', '#cart-selection', function () {
            $(this).addClass('active-btn-in-cart');
        });

        $('body').on('click', '#order-create', function () {
            $(this).addClass('active-btn-in-cart');
        });

        $('body').on('click', '#thanks-selection', function () {
            $(this).addClass('active-btn-in-cart');
        });

});