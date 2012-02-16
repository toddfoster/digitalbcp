/* Author: Todd Foster
Begun 12 Feb 2012
*/

/* global boidem */
boidem = {};

boidem.getUrlParameter = function gup(name)
{
  // source: http://www.netlobo.com/url_query_string_javascript.html
  name = name.replace(/[\[]/,"\\\[").replace(/[\]]/,"\\\]");
  var regexS = "[\\?&]"+name+"=([^&#]*)";
  var regex = new RegExp( regexS );
  var results = regex.exec( window.location.href );
  if( results == null )
    return "";
  else
    return results[1];
}

boidem.bcp = (function() {


  var pageNumber = (function() {
    var currentPage = 0,
      minPage=0,
      maxPage=966;
    // TODO get maxPage from DOM (using jquery's last function)

    var pageNumberSelector = (function(n) {
      return '#page' + n;
    });

    return {
    set: function(n) {
      // ensure n is in legal range
      n = Math.min(n, maxPage);
      n = Math.max(n, minPage);
      $(pageNumberSelector(currentPage)).hide();
      currentPage = n;
      $(pageNumberSelector(currentPage)).show();
      $('#navigationInfo').html('Page ' + currentPage + '/' + maxPage);
    },
    increment: function() {
      this.set(currentPage+1);
    },
    decrement: function() {
      this.set(currentPage-1);
    },
    tableOfContents: 5,
    titlePage: 3
  }}());

  var loadFinished = (function() {
      pageNumber.set(boidem.getUrlParameter('page') || boidem.getUrlParameter('pg') || pageNumber.titlePage);
      $('#navigateLeft').click(function() { pageNumber.decrement(); } );
      $('#navigateRight').click(function() { pageNumber.increment(); } );
  });
  
  return {
    onDocumentReady:function() {
      $('div').html("Loading the BCP...");
      $('div').load('bcp.html', loadFinished);
    }
  }
}());

$(document).ready(boidem.bcp.onDocumentReady);

