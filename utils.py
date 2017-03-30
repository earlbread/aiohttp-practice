import trafaret as T

primitive_ip_regexp = r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$'

TRAFARET = T.Dict({
    T.Key('host'): T.String(regex=primitive_ip_regexp),
    T.Key('port'): T.Int(),
})
