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


  let button1 = document.getElementById("img1")
  

  button1.addEventListener("click", function() {
    window.location.href = "https://www.facebook.com";
  })

  let button2 = document.getElementById("img2")

  button2.addEventListener("click", function() {
    window.location.href = "https://gmail.com";
  })

  let button3 = document.getElementById("img3")

  button3.addEventListener("click", function() {
    window.location.href = "https://instagram.com"
  })
  