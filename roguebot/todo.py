"""
Total work to be done...


- Decider systems (propose an action for each subsystem)
-- Read about RNNs and shit first so you don't do this all dumb-like.
-- Food
-- Move / attack
-- Equipment
-- Scrolls
-- Potions


- Game loop management (tmux / screenshotting?)
-- How to make this fast?
-- How to query inventory?



- Game data management (process screenshot into data usable by decider)

-- Parse:
--- health
--- strength
--- food
--- depth
--- level
--- exp
--- inventory contents
--- rel pos of:
---- Monsters
---- Stairs
---- Gold
---- Items on ground

-- Record:
--- monster health info (based on times hit)


Forecasting vs. training:
- Skinneresque training will get us where we need to be eventually
- What about having an AI that just forecasts where we'll be after a certain action?
-- "not dead" would be a nice outcome
-- We can train the forecasting AI in a skinner fashion.
-- How many moves ahead should it try to predict?
"""
