function config(){
  const settings = YAML.load('settings.yml')
  var config = `${settings.api.protocol}://${settings.api.domain_name}`;
  return config;
}