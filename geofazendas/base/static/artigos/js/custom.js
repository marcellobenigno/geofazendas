jQuery(document).ready(function ($) {


    "use strict";


    // Page loading animation

    $("#preloader").animate({
        'opacity': '0'
    }, 600, function () {
        setTimeout(function () {
            $("#preloader").css("visibility", "hidden").fadeOut();
        }, 300);
    });


    $(window).scroll(function () {
        var scroll = $(window).scrollTop();
        var box = $('.header-text').height();
        var header = $('header').height();

        if (scroll >= box - header) {
            $("header").addClass("background-header");
        } else {
            $("header").removeClass("background-header");
        }
    });

    if ($('.owl-clients').length) {
        $('.owl-clients').owlCarousel({
            loop: true,
            nav: false,
            dots: true,
            items: 1,
            margin: 30,
            autoplay: false,
            smartSpeed: 700,
            autoplayTimeout: 6000,
            responsive: {
                0: {
                    items: 1,
                    margin: 0
                },
                460: {
                    items: 1,
                    margin: 0
                },
                576: {
                    items: 3,
                    margin: 20
                },
                992: {
                    items: 5,
                    margin: 30
                }
            }
        });
    }

    if ($('.owl-banner').length) {
        $('.owl-banner').owlCarousel({
            loop: true,
            nav: true,
            dots: true,
            items: 3,
            margin: 10,
            autoplay: false,
            smartSpeed: 700,
            autoplayTimeout: 6000,
            responsive: {
                0: {
                    items: 1,
                    margin: 0
                },
                460: {
                    items: 1,
                    margin: 0
                },
                576: {
                    items: 1,
                    margin: 10
                },
                992: {
                    items: 3,
                    margin: 10
                }
            }
        });
    }

});


/*
	Create SLUG from a string
	This function rewrite the string prototype and also
	replace latin and other special characters.
	Forked by Gabriel Froes - https://gist.github.com/gabrielfroes
	Original Author: Mathew Byrne - https://gist.github.com/mathewbyrne/1280286
 */
if (!String.prototype.slugify) {
    String.prototype.slugify = function () {

        return this.toString().toLowerCase()
            .replace(/[àÀáÁâÂãäÄÅåª]+/g, 'a')       // Special Characters #1
            .replace(/[èÈéÉêÊëË]+/g, 'e')        // Special Characters #2
            .replace(/[ìÌíÍîÎïÏ]+/g, 'i')        // Special Characters #3
            .replace(/[òÒóÓôÔõÕöÖº]+/g, 'o')        // Special Characters #4
            .replace(/[ùÙúÚûÛüÜ]+/g, 'u')        // Special Characters #5
            .replace(/[ýÝÿŸ]+/g, 'y')            // Special Characters #6
            .replace(/[ñÑ]+/g, 'n')                // Special Characters #7
            .replace(/[çÇ]+/g, 'c')                // Special Characters #8
            .replace(/[ß]+/g, 'ss')                // Special Characters #9
            .replace(/[Ææ]+/g, 'ae')                // Special Characters #10
            .replace(/[Øøœ]+/g, 'oe')            // Special Characters #11
            .replace(/[%]+/g, 'pct')                // Special Characters #12
            .replace(/\s+/g, '-')                // Replace spaces with -
            .replace(/[^\w\-]+/g, '')            // Remove all non-word chars
            .replace(/\-\-+/g, '-')                // Replace multiple - with single -
            .replace(/^-+/, '')                    // Trim - from start of text
            .replace(/-+$/, '');            		// Trim - from end of text

    };
}