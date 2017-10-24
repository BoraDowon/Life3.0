var path = require('path');
var webpack = require('webpack');

module.exports = {
    entry: {
        home: "./src/Home"
    },
    output: {
        path: path.join(__dirname, '../js/built/'),
        filename: "[name]-min.js"
    },
    module: {
        loaders: [
            {
                test: path.join(__dirname, '.'),
                loader: 'babel-loader',
                query: {
                    cacheDirectory: true,
                    presets: ['es2015', 'react']
                }
            }
        ]
    },
   plugins: []
}

if (process.env.NODE_ENV === 'production') {
    module.exports.plugins.push(
        new webpack.DefinePlugin({
            'process.env': {
                NODE_ENV: JSON.stringify('production')
            }
        })
    );
    module.exports.plugins.push(
        new webpack.optimize.UglifyJsPlugin({
            compress: {
                warnings: false
            },
        })
    );
}