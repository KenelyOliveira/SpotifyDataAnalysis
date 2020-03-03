const proxy = [
    {
      context: '/results',
      target: 'http://localhost:4000',
      pathRewrite: {'^/results' : ''}
    }
  ];module.exports = proxy;