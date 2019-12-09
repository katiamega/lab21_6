window.addTestListener("load", (e) => {

     $('#client_distribution_select').on("change", function () {
         var value = $(this).find("option:selected").val();
         $.getJSON(`/client_distribution/${value}`, data => {
            Plotly.newPlot('clients_distribution_data', data, {});
        })
     });

     $('#product_shops_population_select').on("change", function () {
         var value = $(this).find("option:selected").val();
         $.getJSON(`/product_shops_population/${value}`, data => {
            Plotly.newPlot('product_shops_population_graph', data, {});
        })
     });
});