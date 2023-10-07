# To substitute Tags in the following formats:

### Yaml file
```
    tag_name: tag_value
```
 or 

```
    tags:
        - key: tag_key
          value: tag_value
```

### Terraform file
```
locals {
    common_tags = {
        tag_name = tag_value
  }
}
```