export default (req, res) => {
  const verification = req.query['hub.challenge'];

  res.status(200).send(verification);
};
