// * jQuery Cookie Plugin v1.4.1
// * https://github.com/carhartl/jquery-cookie
// *
// * Copyright 2006, 2014 Klaus Hartl
// * Released under the MIT license
// */

(function(factory){if(typeof define==='function'&&define.amd){define(['jquery'],factory)}else if(typeof exports==='object'){module.exports=factory(require('jquery'))}else{factory(jQuery)}}(function($){var pluses=/\+/g;function encode(s){return config.raw?s:encodeURIComponent(s)}
function decode(s){return config.raw?s:decodeURIComponent(s)}
function stringifyCookieValue(value){return encode(config.json?JSON.stringify(value):String(value))}
function parseCookieValue(s){if(s.indexOf('"')===0){s=s.slice(1,-1).replace(/\\"/g,'"').replace(/\\\\/g,'\\')}
try{s=decodeURIComponent(s.replace(pluses,' '));return config.json?JSON.parse(s):s}catch(e){}}
function read(s,converter){var value=config.raw?s:parseCookieValue(s);return $.isFunction(converter)?converter(value):value}
var config=$.cookie=function(key,value,options){if(arguments.length>1&&!$.isFunction(value)){options=$.extend({},config.defaults,options);if(typeof options.expires==='number'){var days=options.expires,t=options.expires=new Date();t.setMilliseconds(t.getMilliseconds()+days*864e+5)}
return(document.cookie=[encode(key),'=',stringifyCookieValue(value),options.expires?'; expires='+options.expires.toUTCString():'',options.path?'; path='+options.path:'',options.domain?'; domain='+options.domain:'',options.secure?'; secure':''].join(''))}
var result=key?undefined:{},cookies=document.cookie?document.cookie.split('; '):[],i=0,l=cookies.length;for(;i<l;i++){var parts=cookies[i].split('='),name=decode(parts.shift()),cookie=parts.join('=');if(key===name){result=read(cookie,value);break}
if(!key&&(cookie=read(cookie))!==undefined){result[name]=cookie}}
return result};config.defaults={};$.removeCookie=function(key,options){$.cookie(key,'',$.extend({},options,{expires:-1}));return!$.cookie(key)}}))


fancyLang={
 lang: "ru",
    i18n: {
        ru: {
            CLOSE: "Закрыть",
            NEXT: "Далее",
            PREV: "Назад",
            ERROR: "Не удается загрузить ресурс",
            PLAY_START: "Запустить слайдшоу",
            PLAY_STOP: "Пауза",
            FULL_SCREEN: "На полный экран",
            THUMBS: "Превью",
            DOWNLOAD: "Скачать",
            SHARE: "Поделиться",
            ZOOM: "Масштаб"
        }
    }
};

$('document').ready(function() {
    $.mobilePanel({ 'navbar': '.b-nav-top' });



    // if (typeof($.cookie('cookieName')) == "undefined") {
    //     setTimeout(function() {
    //         $.fancybox.open($('.baner'));
    //         $.cookie('cookieName', 'cookieName', { expires: 1, path: '/' });
    //       }, 1000);
    // }
  
    // $('.baner-btn').on('click', function (e) {
    //     $.cookie('cookieName', 'cookieName', { expires: 7, path: '/' });
    //     location.reload();  
    //     $.fancybox.close();
    // });


$(window).scroll(function(){
	if($(window).scrollTop()>150){
		$(".b-back-to-top").fadeIn(500);
	}else{
		$(".b-back-to-top").fadeOut(500);
	}
});


$(".b-back-to-top").click(function () {
	$("body, html").animate({
		scrollTop: 0
	}, 800);
	return false;
});

if ($('.ymap')){
    
    $('.ymap').each(function(i){
        var id = 'map-' + i;
        $(this).attr('id', id);
        renderMap(id, $(this).attr('data-coord'), $(this).attr('data-content'), $(this).attr('data-hint') );
    });
}

function renderMap(id, coord, content, hint){
    ymaps.ready(function () {
        
        coordBallun = coord.split(",");

        coordCenter = coord.split(",");
        coordCenter[1] = parseFloat(coordCenter[1])+0.002;

        var myMap = new ymaps.Map(id, {
            center: coordCenter,
                zoom: 15
            }, {
                searchControlProvider: 'yandex#search'
            });

            //Создаём макет содержимого.
            MyIconContentLayout = ymaps.templateLayoutFactory.createClass(
                '<div style="color: #FFFFFF; width: 176px; text-align: center; font-size: 14px; font-family: Conv_GothamProRegular; white-space:nowrap"><i class="icon-palma"></i> <span>$[properties.iconContent]</span></div>'
            );


        myPlacemarkWithContent = new ymaps.Placemark(coordBallun, {
                hintContent: '',
                balloonContent: hint,
                iconContent: content
            }, {
                iconLayout: 'default#imageWithContent',
                iconImageHref: '/template/i/point.png',
                iconImageSize: [206, 50],
                // Смещение левого верхнего угла иконки относительно
                // её "ножки" (точки привязки).
                iconImageOffset: [-27, -50],
                // Смещение слоя с содержимым относительно слоя с картинкой.
                iconContentOffset: [8, 8],
                iconContentLayout: MyIconContentLayout
                });

        myMap.geoObjects.add(myPlacemarkWithContent);
   });
}




    if ($('.partners__list .partners__item').length>2) {
        $('.partners__list').slick({
            dots: false,
            infinite: true,
            autoplay: true,
            arrows: true,
            speed: 1500,
            autoplaySpeed: 4000,
            slidesToShow: 8,
            slidesToScroll: 1,
            responsive: [
                {
                    breakpoint: 1025,
                    settings: {
                        slidesToShow: 5,
                        adaptiveHeight: true
                    }
                },
                {
                    breakpoint: 568,
                    settings: {
                        slidesToShow: 1,
                        arrows: false,
                        slidesToScroll: 1,
                        adaptiveHeight: true
                    }
                }
            ]            

        });
    }


 $('.populartour2').slick({
            dots: false,
            infinite: true,
            autoplay: true,
            arrows: true,
            speed: 1500,
            autoplaySpeed: 4000,
            slidesToShow: 3,
            slidesToScroll: 1,
            responsive: [
                {
                    breakpoint: 1025,
                    settings: {
                        slidesToShow: 5,
                        adaptiveHeight: true
                    }
                },
                {
                    breakpoint: 568,
                    settings: {
                        slidesToShow: 1,
                        arrows: false,
                        slidesToScroll: 1,
                        adaptiveHeight: true
                    }
                }
            ]            

        });
        $('.images2345').slick({
            dots: false,
            infinite: true,
            autoplay: true,
            arrows: true,
            speed: 1500,
            autoplaySpeed: 4000,
            slidesToShow: 2,
            slidesToScroll: 1,
            responsive: [
                {
                    breakpoint: 1000,
                    settings: {
                        slidesToShow: 2,
                        adaptiveHeight: true
                    }
                },
                {
                    breakpoint: 780,
                    settings: {
                        slidesToShow: 1,
                        arrows: false,
                        slidesToScroll: 1,
                        adaptiveHeight: true
                    }
                }
            ]            

        });
        
        
         $('.images21312п').slick({
            dots: false,
            infinite: true,
            autoplay: true,
            arrows: true,
            speed: 1500,
            autoplaySpeed: 4000,
            slidesToShow: 1,
            slidesToScroll: 1,
            responsive: [
                {
                    breakpoint: 1000,
                    settings: {
                        slidesToShow: 1,
                        adaptiveHeight: true
                    }
                },
                {
                    breakpoint: 780,
                    settings: {
                        slidesToShow: 1,
                        arrows: false,
                        slidesToScroll: 1,
                        adaptiveHeight: true
                    }
                }
            ]            

        });
        
        
///////


    $(".trigger-file").click(function() {
        $(this).siblings("[type='file']").trigger("click");
    });

    $(".jot-form input[type='file'][name='avatar']").change(function() {
        $(".jot-form input[type='hidden'][name='avatar']").val($(this).val());
        var filename = $(this).val().split(/(\\|\/)/g).pop();
        $(".jot-form .filename").html(filename);
    });

    /*tabs*/
    $('.b-tabs:not(".searches") .tabs__item:first-child').addClass('active');
    $('.b-tabs:not(".searchess") .tabs__content:first-child').addClass('active');
    $('.b-tabs:not(".searches") .tabs__item').on('click', function() {
        parent = $(this).parents('.b-tabs');
       
        $('.tabs__item', parent).removeClass('active');
        $(this).addClass('active');

        $('.tabs__content', parent).removeClass('active');
        $('.tabs__content', parent).eq($(this).index()).addClass('active');

    });




    /*MAIN SLIDER*/
    if ($('.main-slider__list').length) {
        $('.main-slider__list').slick({
            lazyLoad: 'ondemand',
            dots: true,
            infinite: true,
            autoplay: true,
            arrows: true,
            speed: 1500,
            autoplaySpeed: 4000,
            fade: true,
            cssEase: 'linear',
            responsive: [
                {
                    breakpoint: 1024,
                    settings: {
                        arrows: false,
                    }
                }
               
            ]     

        });
    }
    
     /*MAIN SLIDER*/


    /* ex Slider*/
    if ($('.b-ex-slider').length) {
        //1. генерируем превью
        var slider = $('.b-ex-slider');
        var parent = 'slider-1';
        var sliderCount = $('.ex-slider__item', slider).length;
 
        if ($('.ex-slider__item', slider).length) {
            //self = this;

            //1. запускаем основной слайдер
            if (sliderCount > 9){
                var asNavFor = '#' + parent + ' .ex-slider__thumbs';
            } else {
                asNavFor='';
            }

            $('.ex-slider__list').slick({
                lazyLoad: 'ondemand',
                fade: true,
                cssEase: 'linear',
                asNavFor: asNavFor,
                autoplay: true
            });

            //2. запускаем слайдер превью

            if (sliderCount>4){
            $('.ex-slider__thumbs').slick({
                slidesToShow: 4,
                slidesToScroll: 1,
                asNavFor: '#' + parent + ' .ex-slider__list',
                focusOnSelect: true,
                centerMode: true
            });
            } else {
                $('.ex-slider__thumbs', slider).hide();
            }
            //3. вешаем фанси
           
            // $('.ex-slider__list a', slider).fancybox({
            // 'transitionIn'  : 'elastic',
            // 'transitionOut' : 'elastic',
            // 'speedIn'   : 600, 
            // 'speedOut'    : 200, 
            // 'overlayShow' : false
            // });
            
        }

    } else {
        $('.b-ex-slider').hide()
    }


    //inputmask
    $('.phonemask').inputmask("+7 (999) 999-99-99");

    /*Открыть попап формы зазказа звонка */
     $('.js-callback-btn').on('click', function() {
         $.fancybox.open($('.popup_callback'), fancyLang);
         return false;
     })

	
	  



});
// document redy


/* common form sender */
	
/* protect */
$('.form__protect').val('19X84-lider12');
 
 $('.js-form-submit').on('submit', function(){
     var form=$(this);
     var error=$(this).parent().find('.form__error');
     var success=$(this).parent().find('.form__success');
     var url=$(this).attr('action');
     var submit=$('.form__submit', this);
 
   
	 
     error.hide();
     success.hide();
     submit.prop('disable', true);


	 
     $.ajax({
         url: url,
         type: "post",
         data: $(this).serialize(),
         dataType: 'json',
         success: function(response) {
             if (response.status == 'success') {
                 error.hide();
                 submit.prop('disable', false);
                 form.slideUp(300, function() {
                     success.slideDown();
                 });
                 setTimeout(function() {
                    //  $.fancybox.close();
                     form.slideDown();
                     success.hide();
                 }, 10000);
                 
             } else {
                 error.show();
             }
             
         }
     }).fail(function(response) {
         error.show();
         console.log(response);
     });
 
     return false;
 });

 /* fancybox */

// $('.fancybox').fancybox(fancyLang);


/* calendar */

try {
    // search form: calendar calendar
    flatpickr = flatpickr || { l10ns: {} };
    flatpickr.l10ns.ru = {};

    flatpickr.l10ns.ru.firstDayOfWeek = 1; // Monday

    flatpickr.l10ns.ru.weekdays = {
        shorthand: ['Вс', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб'],
        longhand: ['Воскресенье', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
    };

    flatpickr.l10ns.ru.months = {
        shorthand: ['Янв', 'Фев', 'Март', 'Апр', 'Май', 'Июнь', 'Июль', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек'],
        longhand: ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    };
    flatpickr.l10ns.ru.rangeSeparator = ' - ';
    flatpickr.l10ns.ru.scrollTitle = "Прокрутите колесом для изменения";
    if (typeof module !== "undefined") {
        module.exports = flatpickr.l10ns;
    }

    flatpickr.localize(flatpickr.l10ns.ru);

    $('.js-datepicker').flatpickr({

        dateFormat: "d.m.y",
        minDate: "today",
    });
} catch (e) { }



/* sticky */
stickyNav = function (navbar, minWidth) {
    navbar = document.querySelector(navbar);
    sticky = navbar.offsetTop;
    minWidth = minWidth ? minWidth : 768;

    function onScroll() {
        if (sticky == 0) { sticky = navbar.offsetTop}
        windowWinth = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
        if ((window.pageYOffset >= sticky) && (windowWinth > minWidth)) {
           
            navbar.classList.add("sticky");
        } else {
            navbar.classList.remove("sticky");
        }
    }

    document.addEventListener('scroll', onScroll);
}
stickyNav('.b-nav-top', 769);



/* nav-top toggle item  */

$('.js-nav-top__toggle-item').on('click', function(){
    $(this).parent().toggleClass('opened');
});


/* Search */

/*SEARCH*/
/*
$('.js-search-form').on('submit', function(){
	
	$.ajax({
		url: $(this).attr('action'),
		type: 'GET',
		data: $(this).serialize(),
	})
	.done(function(data) {
		$('.b-search-result, .b-search-result1').html(data);
		$('.ditto_pages').hide();
		$('.b-smallfilter+.u-content h2').hide();

		$("body, html").animate({
			//scrollTo: $('.b-search-result')[0].scrollIntoView(true)
		}, 800);


	}).fail(function(data) {
		console.log('error');
	});

	return false;
});
*/

checkboxList={
	closeAll:function(){
		$('.checkbox-list-wr').hide();
	},
	setCount:function(parent){
        var count = $('input[type="checkbox"]:not(".js-checkbox-list__checkbox--any"):checked', parent).length;
     
        
		if (count){
			parent.parents('.search__field').find('.js-choiseToggle').text('Выбрано [' + count + ']');
            $(".js-checkbox-list__checkbox--any").prop('checked', false);
        } else {
    
            parent.parents('.search__field').find('.js-choiseToggle').text(parent.parents('.search__field').find('.js-choiseToggle').attr('data-label'));
            $(".js-checkbox-list__checkbox--any").prop('checked', 'checked');
		}
	},
	init:function(){
		
		$('.js-choiseToggle').on('click', function(){
			checkboxList.closeAll();
			$(this).next().slideToggle();
		});

		$('.checkbox-list__close').on('click', function(){
			$(this).parent().hide();
		})

		$('html').click(function(e){
		   if($(e.target).parents('.search__field').length == 0 ||  $(e.target).parents('.search__submit-wr').length != 0) {
			 checkboxList.closeAll();
		   }
		});

        $('.checkbox-list input[type="checkbox"]').change(function(){
            var list = $(this).parent().parent();                                                                              
            if ($(this).val() == 0) {
                $('input[type="checkbox"]:not(".js-checkbox-list__checkbox--any")', list).prop('checked', false);
			  } else {
                $(".js-checkbox-list__checkbox--any", list).prop('checked', false);
			  }
			  checkboxList.setCount(list.eq(0));
		});  
        
        $('.checkbox-list').each(function(){
            checkboxList.setCount($(this));
        })
	
	}
};

checkboxList.init();


try {
	
	region = new URL(document.location).searchParams;
	duration = new URL(document.location).searchParams;
	dates = new URL(document.location).searchParams;
	priceTo = new URL(document.location).searchParams;
	priceFrom = new URL(document.location).searchParams;
	
    $('.search__duration--from option').each(function() {
        if ($(this).attr('value') == duration.get("durationFrom")) {
            $(this).prop('selected', true);
        }
    });
	
	$('.search__duration--to option').each(function() {
        if ($(this).attr('value') == duration.get("durationTo")) {
            $(this).prop('selected', true);

        }
    });
	/*
    $('.checkbox-list__checkbox:checked:not(.js-checkbox-list__checkbox--any)').each(function () {
		
		var count = $('.checkbox-list__checkbox:checked', this).length;
		
		if ($(this).attr('checked') == region.get("region[]")) {
			$(this).attr('checked');
		}
		
		$('.js-choiseToggle').text('Выбрано [' + count + ']');
	});
*/
	
	$('.search__date').val(dates.get("dates"));
	
	$('.search__price--from').val(priceFrom.get("priceFrom"));
	
	$('.search__price--to').val(priceTo.get("priceTo"));
	
		
} catch (err) {

}

$(function(){	
	
	$('.js-search__date').daterangepicker({
		autoClose: true,
		format: 'DD.MM.YYYY',
		separator: ' - ',
		startOfWeek: 'monday',
		minDays: 0,
		maxDays: 0,
		autoUpdateInput:false,
		autoApply: true,
		"locale":  {
			"format": "DD.MM.YYYY",
			"separator": " - ",
			"applyLabel": "Apply",
			"cancelLabel": "Cancel",
			"fromLabel": "From",
			"toLabel": "To",
			"customRangeLabel": "Custom",
			"weekLabel": "W",
			"daysOfWeek": [
			"ПН",
			"ВТ",
			"СР",
			"ЧТ",
			"ПТ",
			"СБ",
			"ВС"
			],
			"monthNames": [
			"Январь",
			"Февраль",
			"Март",
			"Апрель",
			"Май",
			"Июнь",
			"Июль",
			"Август",
			"Сентябрь",
			"Октябрь",
			"Ноябрь",
			"Декабрь"
			],
			"firstDay": 1
		},
		"linkedCalendars": false,
		//"alwaysShowCalendars": true,
		//startDate: moment(new Date()).add(1,'days').format('DD.MM.YYYY'),
		//"endDate": moment(new Date()).add(2,'days').format('DD.MM.YYYY')
	});

	$('.js-search__date').on('apply.daterangepicker', function(ev, picker) {
		$('.js-search__date').val(picker.startDate.format('DD.MM.YYYY')+' - '+picker.endDate.format('DD.MM.YYYY'));
	  });
});

// Раскрытие всех дат в турах
$('.atours__alldates').on('click', function () {

    $(this).parent().prev().toggleClass('active');
    return false;
});
