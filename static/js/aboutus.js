(function($) { 
    $(function() { 
  
      //  open and close nav 
      $('#navbar-toggle').click(function() {
        $('nav ul').slideToggle();
      });
  
  
      // Hamburger toggle
      $('#navbar-toggle').on('click', function() {
        this.classList.toggle('active');
      });
  
  
      // If a link has a dropdown, add sub menu toggle.
      $('nav ul li a:not(:only-child)').click(function(e) {
        $(this).siblings('.navbar-dropdown').slideToggle("slow");
  
        // Close dropdown when select another dropdown
        $('.navbar-dropdown').not($(this).siblings()).hide("slow");
        e.stopPropagation();
      });
  
  
      // Click outside the dropdown will remove the dropdown class
      $('html').click(function() {
        $('.navbar-dropdown').hide();
      });
    }); 
  })(jQuery); 



  let button1 = document.getElementById("button1");
  let button2 = document.getElementById("button2");
  let button3 = document.getElementById("button3");

  button1.addEventListener("click", function(){
    window.open("https://www.linkedin.com/in/kris-narola-5260b0200", "_blank");
  })
  button2.addEventListener("click", function(){
    window.open("https://www.linkedin.com/in/vatsal-chauhan024/", "_blank")
  })
  button3.addEventListener("click", function(){
    window.open("https://www.linkedin.com/in/lakhani-vivek-a7290b1ba/", "_blank")
  })
  