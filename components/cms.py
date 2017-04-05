from meya import Component


class CMS(Component):

    def start(self):
        space = self.properties.get("space")
        key = self.properties.get("key")
        language = self.properties.get("language")
        assert space and key, "space and key are required."

        # get languages
        if language:
            languages = [language]
        else:
            languages = self.cms.languages()
        print languages

        # get the entity
        value, entity = self.cms.get(space, key, languages=languages)
        print value
        print entity

        # attach the entity to the message for tracking/training
        message = self.create_message(text=value, entities=[entity])

        # return message
        return self.respond(message=message, action="next")
