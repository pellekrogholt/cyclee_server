/*global define: true */

define(['backbone', 'Trace'], function (Backbone, Trace) {
    'use strict';

    var Traces = Backbone.Collection.extend({
        models: Trace,
        url: '/traces'
    });

    return Traces;
});